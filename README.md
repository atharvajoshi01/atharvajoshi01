<div align="center">
  <h1>Atharva Joshi</h1>
  <p><strong>I build ML systems where mistakes are expensive.</strong></p>
  <p>
    AI governance for regulated environments.<br/>
    Quant systems for fast markets.<br/>
    Evaluation tooling for agents that need to be measured, not admired.
  </p>
  <p>
    <a href="https://linkedin.com/in/atharvajoshi01"><img src="https://img.shields.io/badge/LinkedIn-0A66C2?style=for-the-badge&logo=linkedin&logoColor=white" alt="LinkedIn"/></a>
    <a href="mailto:atharvaj2112@gmail.com"><img src="https://img.shields.io/badge/Email-111111?style=for-the-badge&logo=gmail&logoColor=white" alt="Email"/></a>
  </p>
</div>

<p align="center">
  <img src="https://img.shields.io/badge/Base-New_York-111111?style=flat-square" alt="Base: New York"/>
  <img src="https://img.shields.io/badge/Primary-Python-1f6feb?style=flat-square" alt="Primary: Python"/>
  <img src="https://img.shields.io/badge/Systems-C%2B%2B20-0b5fff?style=flat-square" alt="Systems: C++20"/>
  <img src="https://img.shields.io/badge/Stack-TypeScript%20%7C%20SQL-2f855a?style=flat-square" alt="Stack: TypeScript and SQL"/>
</p>

## Thesis

Most ML profiles are a pile of models, notebooks, and dashboards.

That is not what I am optimizing for.

I care about systems that operate under constraint:

- `regulation`: explainability, audit trails, fairness checks, policy-aware tooling
- `latency`: order books, execution infrastructure, market microstructure
- `reliability`: evaluation harnesses, failure analysis, safety checks for agents

If a system has compliance pressure, real money, or operational blast radius, that is usually where I want to work.

## Build Surface

| Area | What I build | Representative repo |
| --- | --- | --- |
| `AI governance` | Regulation-aware ML pipelines, model reporting, drift and fairness checks | [finreg-ml](https://github.com/atharvajoshi01/finreg-ml) |
| `Agent evaluation` | Tooling to measure cost, latency, safety, and behavior across agent systems | [agenteval](https://github.com/atharvajoshi01/agenteval) |
| `Quant systems` | Pricing engines, order book infrastructure, execution-oriented research systems | [Atlas](https://github.com/atharvajoshi01/Atlas), [deep-galerkin-pricing](https://github.com/atharvajoshi01/deep-galerkin-pricing) |

## Selected Builds

### [finreg-ml](https://github.com/atharvajoshi01/finreg-ml)

Train a model, get governance attached to it from day one.

Built for teams that need more than a validation score before shipping ML into regulated workflows.

`Python` · `scikit-learn` · `SHAP` · `Pydantic`

### [agenteval](https://github.com/atharvajoshi01/agenteval)

Evaluation framework for AI agents with explicit checks for cost, latency, and safety.

Built for comparing agent systems like engineering artifacts instead of demo theater.

`Python` · `Pydantic` · `asyncio` · `tiktoken`

### [Atlas](https://github.com/atharvajoshi01/Atlas)

Low-latency order book engine with a C++ core and a Python research layer.

Built around the kind of system constraints that actually matter in execution infrastructure.

`C++20` · `Python` · `XGBoost`

### [deep-galerkin-pricing](https://github.com/atharvajoshi01/deep-galerkin-pricing)

Neural PDE solver for option pricing using the Deep Galerkin Method.

Built at the intersection of quantitative finance, numerics, and modern ML tooling.

`PyTorch` · `Quantitative Finance` · `Differential Equations`

## Open Source Receipts

These are not vague contribution claims. These are the actual PRs.

- [microsoft/agent-governance-toolkit#776](https://github.com/microsoft/agent-governance-toolkit/pull/776) `merged`
  Promoted `EUAIActRiskClassifier` from example code into the library with tests and external config.
- [microsoft/agent-governance-toolkit#786](https://github.com/microsoft/agent-governance-toolkit/pull/786) `merged`
  Added docs, examples, changelog, and README support for the classifier.
- [AI4Finance-Foundation/FinRL#1410](https://github.com/AI4Finance-Foundation/FinRL/pull/1410) `merged`
  Fixed incorrect `threading.Thread` target invocation in paper trading.
- [google/tf-quant-finance#113](https://github.com/google/tf-quant-finance/pull/113) `open`
  Replaced `md5` with `sha256` in a cache-key hashing utility.
- [goldmansachs/gs-quant#345](https://github.com/goldmansachs/gs-quant/pull/345) `open`
  Fixed pandas 2.x compatibility by replacing removed `.append()` calls.
- [sktime/sktime#9809](https://github.com/sktime/sktime/pull/9809) `open`
  Fixed `NaiveForecaster.predict_var(cov=True)` returning all-`NaN` covariance matrices.

## Current Direction

- Making regulated ML tooling harder to fake and easier to audit
- Building quant-oriented systems that respect latency and implementation detail
- Treating agent evaluation as an engineering discipline, not a prompt contest

## Contact

- Email: [atharvaj2112@gmail.com](mailto:atharvaj2112@gmail.com)
- LinkedIn: [linkedin.com/in/atharvajoshi01](https://linkedin.com/in/atharvajoshi01)
