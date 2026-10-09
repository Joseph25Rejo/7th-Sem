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
