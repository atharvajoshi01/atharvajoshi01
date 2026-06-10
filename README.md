<div align="center">
  <img src="./assets/field-notes.svg" width="100%" alt="Atharva Joshi field notes header"/>
</div>

<div align="center">

I work on machine learning systems that need to hold up in the real world.

That usually means some mix of regulation, latency, and reliability.

[Portfolio](https://atharvajoshi01.github.io) • [LinkedIn](https://linkedin.com/in/atharvajoshi01) • [Email](mailto:atharvaj2112@gmail.com) • New York

</div>

## What I Work On

| Area | What pulls me in |
| --- | --- |
| `AI governance` | explainability, audit trails, fairness checks, policy-aware tooling |
| `Production RAG` | hybrid retrieval, ensemble generation, evaluation that maps to a real decision |
| `Quant systems` | order books, pricing, execution research, market microstructure |
| `Agent evaluation` | measuring accuracy, latency, cost, and safety before something ships |

I am less interested in building one more polished demo and more interested in building systems that survive constraints.

## Selected Work

| Project | What it is | Live |
| --- | --- | --- |
| [finreg-ml](https://github.com/atharvajoshi01/finreg-ml) | Governance-oriented ML wrapper for explainability, fairness, drift, threshold tuning, and EU AI Act compliance reporting. On PyPI. | [demo](https://huggingface.co/spaces/aadu21/finreg-ml-demo) |
| [talent-rag](https://github.com/atharvajoshi01/talent-rag) | Production-grade RAG: hybrid retrieval (semantic + metadata + keyword), cross-encoder reranking, ensemble generation with judge selection, async index-build pattern. | repo |
| [stocksense](https://github.com/atharvajoshi01/stocksense) | End-to-end demand forecasting with walk-forward CV and a reorder-quality decision metric instead of MAPE alone. | [dashboard](https://stocksense-ajoshs-projects.vercel.app/) |
| [clarify](https://github.com/atharvajoshi01/clarify) | LLM agent that turns a free-text BA brief into a validated artifact pack (requirements, RACI, traceability) without hallucinating. | repo |
| [crypto-stat-arb](https://github.com/atharvajoshi01/crypto-stat-arb) | Cointegration stat-arb on real Kraken data with Kalman hedge ratios and explicit gross vs. net Sharpe analysis. | repo |
| [agenteval](https://github.com/atharvajoshi01/agenteval) | LLM-agent evaluation framework. Comparative against a deterministic baseline, so the deployment decision is one number. | repo |
| [Atlas](https://github.com/atharvajoshi01/Atlas) | C++20 limit order book engine. 62M ops/sec, 16ns insertion, NASDAQ ITCH 5.0 parsing at 258M msg/sec, lock-free ring buffers. | repo |

## How I Like To Build

- start from the failure modes, not the press release
- keep the workflow clear enough that another engineer can audit it
- prefer evidence over posturing
- treat performance and correctness as product features

## Open Source Work

These are actual public PRs. Merged contributions get verifiably attributed on the upstream commit log.

**Merged**

- [microsoft/agent-governance-toolkit#776](https://github.com/microsoft/agent-governance-toolkit/pull/776)
  Promoted `EUAIActRiskClassifier` from example code into the library with structured risk assessment, YAML config, and 24 tests.
- [microsoft/agent-governance-toolkit#786](https://github.com/microsoft/agent-governance-toolkit/pull/786)
  Added docs, examples, changelog, and README support for the classifier.
- [AI4Finance-Foundation/FinRL#1410](https://github.com/AI4Finance-Foundation/FinRL/pull/1410) — 14.6k★
  Fixed incorrect `threading.Thread` target invocation in paper trading across buy/sell/turbulence paths.

**Open and under maintainer review**

- [google/tf-quant-finance#113](https://github.com/google/tf-quant-finance/pull/113) — 5.3k★
  Replaced `md5` with `sha256` in a cache-key hashing utility.
- [goldmansachs/gs-quant#345](https://github.com/goldmansachs/gs-quant/pull/345) — 10k★
  Fixed pandas 2.x compatibility by replacing removed `DataFrame.append` calls.
- [ranaroussi/quantstats#512](https://github.com/ranaroussi/quantstats/pull/512) — 7k★
  Added a `compounded` flag to `calmar()` and `rar()` so intraday and non-compounded streams compute correctly.
- [bukosabino/ta#364](https://github.com/bukosabino/ta/pull/364) — 5k★
  Added IV Rank and IV Percentile indicators for vol-aware position sizing.
- [stefan-jansen/zipline-reloaded#328](https://github.com/stefan-jansen/zipline-reloaded/pull/328) — 1.7k★
  Fixed `DataPortal` correctness bugs: `(None, None)` vs. `None`, and wrong frequency in the daily code path.
- [joshyattridge/smart-money-concepts#103](https://github.com/joshyattridge/smart-money-concepts/pull/103) — 1.4k★
  Fixed look-ahead bias in `swing_highs_lows` that inflated PF from ~1.8 to 7.3 on the reporter's reproducer.
- [kernc/backtesting.py#1359](https://github.com/kernc/backtesting.py/pull/1359)
  Fixed read-only array error in `FractionalBacktest` indicator scaling under pandas 2.x copy-on-write.

## Right Now

- making regulated ML workflows easier to explain and review
- treating agent evaluation like engineering work instead of theater
- moving closer to systems where implementation detail matters

## Recent Activity

<!-- recent_activity_start -->
**Recent commits**

- _no recent personal-repo commits picked up_

**Recent open source PRs**

- [`#103`](https://github.com/joshyattridge/smart-money-concepts/pull/103) `joshyattridge/smart-money-concepts` Fix look-ahead bias in swing_highs_lows `open` <sub>2026-06-08</sub>
- [`#328`](https://github.com/stefan-jansen/zipline-reloaded/pull/328) `stefan-jansen/zipline-reloaded` Fix DataPortal correctness bugs: tuple vs None and wrong frequency `open` <sub>2026-06-08</sub>
- [`#364`](https://github.com/bukosabino/ta/pull/364) `bukosabino/ta` Add Rank and Percentile indicators `open` <sub>2026-06-08</sub>
- [`#1359`](https://github.com/kernc/backtesting.py/pull/1359) `kernc/backtesting.py` Fix read-only array error in FractionalBacktest indicator scaling `open` <sub>2026-06-08</sub>
- [`#512`](https://github.com/ranaroussi/quantstats/pull/512) `ranaroussi/quantstats` Add compounded flag to calmar() and rar() `open` <sub>2026-06-08</sub>

**Recently published repos**

- [`talent-rag`](https://github.com/atharvajoshi01/talent-rag) Production-grade RAG system for talent intelligence — hybrid retrieva… <sub>2026-06-05</sub>
- [`stocksense`](https://github.com/atharvajoshi01/stocksense) End-to-end demand forecasting and inventory health platform for a dis… <sub>2026-05-13</sub>
- [`clarify`](https://github.com/atharvajoshi01/clarify) AI Business Analyst agent — brief in, requirements + RTM + test cases… <sub>2026-05-07</sub>
- [`crypto-stat-arb`](https://github.com/atharvajoshi01/crypto-stat-arb) Statistical arbitrage engine for cryptocurrency markets — cointegrati… <sub>2026-04-13</sub>
- [`agenteval`](https://github.com/atharvajoshi01/agenteval) Lightweight evaluation framework for AI agents — measure accuracy, co… <sub>2026-04-06</sub>

<sub>last updated 2026-06-10 UTC</sub>
<!-- recent_activity_end -->

## Contact

- Email: [atharvaj2112@gmail.com](mailto:atharvaj2112@gmail.com)
- LinkedIn: [linkedin.com/in/atharvajoshi01](https://linkedin.com/in/atharvajoshi01)
- Portfolio: [atharvajoshi01.github.io](https://atharvajoshi01.github.io)
