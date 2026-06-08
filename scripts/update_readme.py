#!/usr/bin/env python3
"""Update the Recent Activity section of README.md.

Pulls three signals from the GitHub API for `atharvajoshi01`:

  1. Last 5 pushed commits across personal repositories
  2. Last 5 merged or open external pull requests
  3. Last 5 created repos

The script writes the rendered block between
`<!-- recent_activity_start -->` and `<!-- recent_activity_end -->` in the
README. It is invoked from `.github/workflows/update-readme.yml`. The
workflow uses the default `GITHUB_TOKEN`, which has the read access needed
for the public endpoints; no PAT required.
"""

from __future__ import annotations

import os
import re
import sys
from datetime import datetime, timezone
from pathlib import Path
from urllib.parse import urlencode
from urllib.request import Request, urlopen

USER = "atharvajoshi01"
README_PATH = Path(__file__).resolve().parent.parent / "README.md"
START = "<!-- recent_activity_start -->"
END = "<!-- recent_activity_end -->"
API = "https://api.github.com"


def _gh(path: str, params: dict | None = None) -> object:
    url = f"{API}{path}"
    if params:
        url = f"{url}?{urlencode(params)}"
    headers = {
        "Accept": "application/vnd.github+json",
        "User-Agent": f"{USER}-profile-readme-bot",
    }
    token = os.environ.get("GITHUB_TOKEN")
    if token:
        headers["Authorization"] = f"Bearer {token}"
    req = Request(url, headers=headers)
    with urlopen(req, timeout=30) as resp:
        import json

        return json.load(resp)


def _short(s: str, n: int) -> str:
    s = (s or "").strip().splitlines()[0] if s else ""
    return s if len(s) <= n else s[: n - 1].rstrip() + "…"


def fetch_recent_commits(limit: int = 5) -> list[str]:
    events = _gh(f"/users/{USER}/events/public", {"per_page": 100})
    lines: list[str] = []
    seen: set[str] = set()
    for e in events:
        if e.get("type") != "PushEvent":
            continue
        repo_full = e["repo"]["name"]
        if "/" not in repo_full:
            continue
        owner, _ = repo_full.split("/", 1)
        if owner != USER:
            continue
        for c in reversed(e["payload"].get("commits", [])):
            msg = _short(c.get("message", ""), 70)
            sha = c.get("sha", "")[:7]
            if not sha or sha in seen:
                continue
            seen.add(sha)
            url = f"https://github.com/{repo_full}/commit/{c.get('sha','')}"
            when = e.get("created_at", "")[:10]
            lines.append(
                f"- [`{sha}`]({url}) `{repo_full}` {msg} <sub>{when}</sub>"
            )
            if len(lines) >= limit:
                return lines
    return lines


def fetch_recent_pull_requests(limit: int = 5) -> list[str]:
    data = _gh(
        "/search/issues",
        {
            "q": f"author:{USER} is:pr -user:{USER} sort:updated",
            "per_page": limit,
        },
    )
    items = data.get("items", []) if isinstance(data, dict) else []
    lines: list[str] = []
    for pr in items[:limit]:
        repo_full = pr["repository_url"].rsplit("/", 2)[-2:]
        repo_full = "/".join(repo_full)
        title = _short(pr.get("title", ""), 70)
        when = (pr.get("updated_at") or pr.get("created_at") or "")[:10]
        state = "merged" if pr.get("pull_request", {}).get("merged_at") else pr.get(
            "state", "open"
        )
        lines.append(
            f"- [`#{pr['number']}`]({pr['html_url']}) `{repo_full}` {title}"
            f" `{state}` <sub>{when}</sub>"
        )
    return lines


def fetch_recent_repos(limit: int = 5) -> list[str]:
    repos = _gh(
        f"/users/{USER}/repos",
        {"per_page": 100, "sort": "created", "direction": "desc"},
    )
    if not isinstance(repos, list):
        return []
    lines: list[str] = []
    for r in repos:
        if r.get("fork") or r.get("archived"):
            continue
        if r.get("name") in {USER, "atharvajoshi01.github.io"}:
            continue
        desc = _short(r.get("description") or "", 70)
        when = (r.get("created_at") or "")[:10]
        lines.append(
            f"- [`{r['name']}`]({r['html_url']}) {desc} <sub>{when}</sub>"
        )
        if len(lines) >= limit:
            break
    return lines


def render_block() -> str:
    now = datetime.now(timezone.utc).strftime("%Y-%m-%d")
    commits = fetch_recent_commits()
    prs = fetch_recent_pull_requests()
    repos = fetch_recent_repos()

    parts: list[str] = []
    parts.append("**Recent commits**\n")
    parts.extend(commits or ["- _no recent personal-repo commits picked up_"])
    parts.append("")
    parts.append("**Recent open source PRs**\n")
    parts.extend(prs or ["- _no recent PRs picked up_"])
    parts.append("")
    parts.append("**Recently published repos**\n")
    parts.extend(repos or ["- _no recent repos picked up_"])
    parts.append("")
    parts.append(f"<sub>last updated {now} UTC</sub>")
    return "\n".join(parts)


def update_readme() -> bool:
    text = README_PATH.read_text(encoding="utf-8")
    if START not in text or END not in text:
        sys.stderr.write(
            "README.md is missing the recent_activity markers; skipping.\n"
        )
        return False
    block = render_block()
    replaced = re.sub(
        rf"{re.escape(START)}.*?{re.escape(END)}",
        f"{START}\n{block}\n{END}",
        text,
        flags=re.DOTALL,
    )
    if replaced == text:
        return False
    README_PATH.write_text(replaced, encoding="utf-8")
    return True


if __name__ == "__main__":
    changed = update_readme()
    print("README updated" if changed else "README unchanged")
