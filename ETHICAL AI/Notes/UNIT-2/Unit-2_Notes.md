# Unit 2 – Bias and Fairness

> **Source:** Bartneck et al., *An Introduction to Ethics in Robotics and AI* – §2.2 (ML & bias), §3.6.2 (bias testing tools), §4.3.4 (Justice: credit, courts, healthcare). The book treats bias briefly; the taxonomy, metrics, mitigation techniques and implementation are standard material marked **[+]**.

## Contents
1. [Understanding bias in data and models](#1-understanding-bias-in-data-and-models)
2. [How bias impacts decision making](#2-how-bias-impacts-decision-making)
3. [Types of bias](#3-types-of-bias)
4. [Real-world cases](#4-real-world-cases)
5. [Detecting bias](#5-techniques-to-detect-bias)
6. [Mitigating bias](#6-techniques-to-mitigate-bias)
7. [Implementation](#7-implementing-bias-detection-and-fairness)
8. [Quick revision](#8-quick-revision)

---

## 1. Understanding Bias in Data and Models

![Justitia – blindfold (impartiality), scales (evidence), sword (punishment)](images/fig4.1_justitia.png)

*Fig 4.1 – Justitia, the symbol of **justice**: the principle that AI should act **justly and without bias**.*

- **Bias** = systematic, unfair skew in outcomes for certain people/groups. **Fairness** = absence of such unjustified discrimination.
- **Where it enters (book §2.2):** supervised learning needs **human-labelled data** → *human and societal biases can be baked into the classifier*. A model trained on past decisions simply **reproduces the past**.
- **Data bias:** unrepresentative samples, skewed labels, missing groups, **proxy variables** (e.g. neighbourhood ↔ race) that leak protected attributes **[+]**.
- **Model bias:** objective function/problem formulation (cost used as a proxy for need), algorithm choices, optimisation for overall accuracy that hides poor performance on minorities **[+]**.
- **Removing the sensitive column is not enough** – other features act as proxies ("fairness through unawareness" fails).
- **Fairness vs accuracy:** blinding algorithms to race may even harm (Kleinberg et al.); data must still reflect "what is the case". Trade-offs must be made consciously by stakeholders.

---

## 2. How Bias Impacts the Decision-Making Process

| Stage | How bias creeps in / its effect |
|---|---|
| Problem formulation | Wrong target/proxy (healthcare *cost* ≠ *need*) |
| Data collection & labelling | Under-representation, historical discrimination in labels |
| Training | Model learns & **amplifies** patterns; optimises majority group |
| Deployment | **Feedback loops** (predictive policing sends more police → more arrests → more "crime data") **[+]** |
| Human use | **Automation bias** – people over-trust "objective" scores |

**Consequences:** unequal access to credit, jobs, healthcare, justice; **loss of trust** (ch. 4) and violation of **justice / non-maleficence**; legal & reputational risk (ch. 6); scale – one biased algorithm affects **millions**.

> Book's discussion question: *we expect AI to be fairer than humans – are there limits?* Yes: it learns from human data, fairness has several conflicting definitions, and a precise algorithm can't fully capture amorphous concepts.

---

## 3. Types of Bias **[+]**

| Type | Meaning | Example |
|---|---|---|
| **Historical bias** | World itself was unequal; data faithfully records it | Few women in past CEO data → model prefers men |
| **Representation / sampling bias** | Training sample doesn't reflect the population | Face data mostly light-skinned → poor accuracy on dark skin |
| **Measurement / label bias** | Proxy or labels measured inconsistently | Arrests used as a proxy for crime; cost for need |
| **Selection bias** | Non-random inclusion of data | Survey only of smartphone users |
| **Algorithmic bias** | Model/objective favours some groups | Optimising overall accuracy; ranking algorithms |
| **Aggregation bias** | One model for groups that differ | Single medical model for all ethnicities |
| **Confirmation / cognitive bias** | Developers' or users' beliefs shape design/interpretation | Choosing features that fit expectations |
| **Automation bias** | Over-reliance on algorithmic output | Judge defers to risk score |
| **Deployment / feedback-loop bias** | System used differently from intent, or its output changes future data | Predictive policing |

---

## 4. Examples of Real-World Cases

| Case | What happened | Lesson |
|---|---|---|
| **COMPAS recidivism** (Broward County, USA) | ProPublica (2016): higher false-positive rates for Black defendants. Northpointe: scores are **predictively fair** given different base rates. Accuracy only ≈ **65%** (Dressel & Farid). *Loomis v. Wisconsin* – defence couldn't inspect the proprietary algorithm; appeal failed | **Fairness definitions conflict** (Chouldechova 2017: predictive parity ⊥ equal FPR/FNR when base rates differ); need explainability |
| **Healthcare risk algorithm** (Obermeyer et al. 2019) | Race excluded, but **healthcare cost** used as proxy for need; poor patients spend less (access, transport, childcare) → Black patients under-flagged; affects millions | **Problem formulation** is the root cause; proxies encode structural inequality |
| **Credit scoring** | Applicant's neighbourhood data → systematic bias against residential areas | Proxy variables; faster decisions can scale unfairness |
| **Amazon recruiting tool** **[+]** | Trained on 10 years of mostly male CVs; penalised CVs mentioning "women's" – scrapped (2018) | Historical bias |
| **Face recognition** **[+]** | *Gender Shades* (Buolamwini & Gebru 2018): much higher error for darker-skinned women | Representation bias |
| **Chatbots/language models** **[+]** | Learn stereotypes and toxicity from web text (e.g. Microsoft Tay) | Training-data bias |

---

## 5. Techniques to Detect Bias

1. **Audit data:** group-wise counts, label rates, missing values, correlation of features with protected attributes (**proxy detection**).
2. **Compare model outcomes across groups** using fairness metrics **[+]** (G = protected group, Ŷ = prediction, Y = truth):

| Metric | Requires | Formula / idea |
|---|---|---|
| **Statistical (demographic) parity** | Equal **selection rate** | P(Ŷ=1 \| G=a) = P(Ŷ=1 \| G=b); report the **difference** |
| **Disparate impact ratio** | Ratio ≥ **0.8** ("80% rule") | selection rate (unprivileged) ÷ selection rate (privileged) |
| **Equal opportunity** | Equal **TPR** | P(Ŷ=1 \| Y=1, G) same across groups |
| **Equalised odds** | Equal **TPR and FPR** | both error rates equal |
| **Predictive parity** | Equal **precision** | P(Y=1 \| Ŷ=1, G) same (COMPAS developers' choice) |
| **Calibration** | Score means same risk for all groups | P(Y=1 \| score=s, G) same |
| **Individual fairness** | Similar individuals → similar outcomes | Lipschitz-style similarity |
| **Counterfactual fairness** | Outcome unchanged if protected attribute flipped | Causal reasoning |

> ⚠️ Metrics **cannot all be satisfied at once** (unless base rates are equal or the classifier is perfect) → pick the metric that fits the context & harm.

3. **Error analysis / slicing** – accuracy, FPR, FNR per subgroup and intersections (e.g. race × gender).
4. **Explainability tools** – feature importance, **SHAP/LIME**, to expose proxy reliance **[+]**.
5. **Toolkits & audits (book §3.6.2):** IBM **AI Fairness 360**, **audit-AI**, Facebook **Fairness Flow**, third-party algorithmic audits (O'Neil Risk Consulting & Algorithmic Auditing), IEEE algorithmic-bias standard project (2017). Also Fairlearn, Google What-If Tool **[+]**.
6. **Diverse test cases & red-teaming**, plus continuous monitoring after deployment.

---

## 6. Techniques to Mitigate Bias **[+]**

Applied at three points of the ML pipeline:

| Stage | Technique | Idea |
|---|---|---|
| **Pre-processing** (fix the data) | Collect more/representative data; **re-sampling**; **reweighing** (weight each (group,label) cell so group ⟂ label); remove/transform proxies; **disparate-impact remover** | Cheapest, model-agnostic |
| **In-processing** (fix the learning) | Add **fairness constraints / regulariser** to the loss; **adversarial debiasing** (adversary tries to predict group from output); fair representation learning | Directly optimises fairness–accuracy trade-off |
| **Post-processing** (fix the output) | **Group-specific thresholds**; equalised-odds post-processing; **reject-option classification** (re-label near-boundary cases) | Works on black-box models, but can be legally sensitive |

**Non-technical measures:** diverse development teams, **fairness requirements** defined with stakeholders, documentation (**datasheets for datasets, model cards**), **human-in-the-loop** review, appeal/redress mechanisms, regular **audits**, legal compliance (GDPR, anti-discrimination law), and honest handling of the **fairness ↔ accuracy trade-off**.
