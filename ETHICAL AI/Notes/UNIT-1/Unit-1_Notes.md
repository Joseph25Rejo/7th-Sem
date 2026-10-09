# Unit 1 – Introduction to AI and Ethics & Core Ethical Principles

> **Source:** Bartneck, Lütge, Wagner, Welsh – *An Introduction to Ethics in Robotics and AI* (Springer, 2021), Ch. 2, 3 and 4.
> Points marked **[+]** are short additions beyond the textbook (to cover syllabus items the book treats lightly).

## Contents
1. [What is AI?](#1-what-is-ai)
2. [Strong vs Weak AI & Types of AI](#2-strong-vs-weak-ai--types-of-ai)
3. [Types of Ethics](#3-types-of-ethics)
4. [Ethics and Law](#4-relationship-between-ethics-and-law)
5. [Machine Ethics, Examples, Moral Diversity & Testing](#5-machine-ethics)
6. [Core Ethical Principles](#6-core-ethical-principles)
7. [Quick Revision & Likely Questions](#7-quick-revision)

---

## 1. What is AI?

- **Definitions**
  - *Kaplan & Haenlein*: a system's ability to **correctly interpret external data, learn from it, and use that learning to achieve goals through flexible adaptation**.
  - *Poole & Mackworth*: the study of computational **agents that act intelligently** – actions suit circumstances and goals, flexible, learn from experience, make good choices under limits.
  - *Russell & Norvig*: study of agents that receive **percepts** and take **actions** (a function mapping percepts → actions).
- **Four schools of thought** (Russell & Norvig): machines that **think like humans**, **act like humans**, **think rationally**, **act rationally**.
- Common core: AI = designing **intelligent agents that achieve goals**. AI is a *moving target* ("AI is whatever computers can't do yet").
- **Autonomy** (context-sensitive, root = *auto-nomos*, "self-rule"): in engineering – operating without a human operator; in bioethics – a patient's right to decide; in Kantian ethics – ability to choose one's own moral rules.

![Fig 2.1 – Siri cannot answer an ethically loaded question](images/fig2.1_siri.png)

*Fig 2.1 – "Should I lie about my weight on my dating profile?" Siri: "I can't answer that." Answering needs speech recognition, language understanding, world knowledge **and** a moral stance (consequentialist: maximise happiness; deontological: lying is a duty violation; virtue: be honest) – so even a "trivial" question is hard.*

### Machine learning (ML)
| Type | Idea | Example |
|---|---|---|
| **Supervised** | Learn from **labelled** data (classification/regression); output is a *classifier*. Measured by true-positive & false-positive rate; needs separate **training / test** sets | Spam filter |
| **Unsupervised** | Find patterns without labels (clustering, PCA) | Customer segmentation |
| **Reinforcement** | Learn a **policy** (action → expected reward) from a reward signal | Robot reaching a goal |

> Bias link: supervised labels are made by humans, so **human/societal bias can enter the classifier** (textbook discussion question).

### Robots & why AI is hard
- **Robot** = AI that is **situated** (real world) and **embodied** (physical body). Works by **Sense → Plan → Act**; errors at one step propagate to the next.
- **System integration** (many sensors/actuators with different failure modes) is one of the hardest parts.
- Hard for AI: limited sensors/perception, **poor generalisation** (face recogniser fails on profile view), **no common sense**, no innate knowledge ("blank slate"), hype cycles.
- **Fiction vs science:** media (HAL, Terminator, Westworld) inflates expectations – the "Frankenstein complex". **Sophia** (Saudi "citizenship", 2017) is mostly scripted PR, not real intelligence.

---

## 2. Strong vs Weak AI & Types of AI

- **Turing Test (1950):** if a human judge cannot tell a machine from a person in conversation, the machine is deemed intelligent. Replaces vague "thinking" with a testable task. *Criticised:* no time limit specified; passing may not be necessary/sufficient for intelligence.
- **Weak (narrow) AI** – one well-defined task (chess, Go, loan scoring). *All current AI.*
- **Strong AI (Searle, 1980)** – a suitably programmed computer *has a mind* in the same sense humans do; general intelligence. **Not yet achieved.**

**Types of AI systems:** *Expert systems* (rule-based, e.g. loan advisors) · *Planning systems* (e.g. SPIKE for Hubble) · *Computer vision* (object recognition) · *Machine learning*.

---

## 3. Types of Ethics

*Ethics* = theory of morality (principles, general norms); *morality* = the actual rules/values/norms guiding actions. Kant: ethics asks **"What should I do?"**

| Branch | Question it answers | Key points |
|---|---|---|
| **Descriptive** | *What do people actually believe/do?* | Empirical (moral psychology, experimental economics). E.g. **ultimatum game** – people sacrifice profit for fairness. Feeds normative ethics. |
| **Normative** | *What ought to be done?* (right/wrong, good/evil) | Claims general validity ("stealing is wrong for everybody"). 3 theories below. |
| **Meta-ethics** | *What is morality itself?* (theory of ethics) | **Ontology** (what has moral worth), **semantics** (meaning of "right/good/ought"), **epistemology** (how we know moral truths). |
| **Applied** | Ethics in concrete fields | Medical, bio-, business ethics. Influence runs **both ways** (practice shapes theory). |

### Three normative theories
| Theory | Judges an action by | Thinker | Running example (company CSR programme) |
|---|---|---|---|
| **Deontological** (duty) | The action itself – intention, duty, rules | **Kant** – *Categorical Imperative*: act only on a maxim you can will as a **universal law** | Critics care about the company's **motive** (PR vs genuine) |
| **Consequentialist** | Foreseeable **consequences** | Bentham, Mill (utilitarianism – maximise happiness) | Motive irrelevant; only the **social impact** counts |
| **Virtue** | The **character** of the agent | Plato (4 cardinal virtues: wisdom, justice, fortitude, temperance), **Aristotle** (11 moral virtues + intellectual) | Is the company acting *honestly/justly*? |

---

## 4. Relationship Between Ethics and Law

- Common view: *"ethics starts where the law ends"* – the book **challenges** this.
  1. **Laws have an ethical side** (anti-pollution, anti-trust laws are also ethical norms).
  2. **Ethics acts as "soft law"** – firms follow ethical standards the law doesn't demand, to protect reputation/stock value (e.g. *fair-trade* coffee as a selling point), with almost the same effect as **hard law**.
- Summary: Law = enforceable minimum; ethics = broader, can precede and shape law (e.g. hate-speech laws on social media).

---

## 5. Machine Ethics

**Machine ethics:** *what would it take to build an AI that can make moral decisions?*
- Machines lack **phenomenology** (feelings, consciousness) and moral intuition – they only process data *about* feelings.
- Critics (van Wynsberghe & Robbins) say roboticists haven't given strong reasons to build "moral robots".

![Fig 3.3 – Sophia: lifelike, but no feelings or consciousness](images/fig3.3_sophia.png)

*Fig 3.3 – Sophia (Hanson Robotics): a lifelike face ≠ moral agency; treated by many as a publicity stunt.*

### 5.1 Machine ethics examples
Pipeline: **sensors → symbol grounding (raw data → symbols) → moral cognition (logic) → action.**
- **Logic = truth-preserving inference** (Socrates is a man, all men are mortal ⇒ Socrates is mortal).
- **Speeding-ticket robot:** rule *"if driver X is speeding then robot is obligated to issue a ticket to X"* + fact "X is speeding" ⇒ issue ticket. Easy – clear rule, clear symbols.
- **Toddler vs letter robot:** a toddler falls into a stream while the robot is going to post a letter. Two duties clash (rescue vs post). Needs **causal understanding** and a **utility scale** (toddler = +1,000,000, on-time letter = +1) → rescue wins.
- **Failure of naive utilitarian arithmetic:** a truck with **1,000,001 letters** (+1 each) outweighs the toddler (1,000,000) → robot lets the toddler drown! Shows simple utility sums give **counter-intuitive** results. *To implement deontology you need a principled way to resolve clashes of duties.*

### 5.2 Moral diversity and testing
- **Core problem:** *no agreement on the correct moral theory* (philosophers split roughly ¼ deontology, ¼ consequentialism, ⅓ virtue – Bourget & Chalmers 2014). What do we implement?
- **Approach – testing:** build many **ethical test cases**; moral competence = ability to pass them; iterating on new cases may expand competence and even give insight into theory.
- **Testing/certifying fairness – tools & efforts:** IEEE standards project on **algorithmic bias** (2017); **AI Fairness 360** (IBM), **audit-AI**; services like O'Neil Risk Consulting & Algorithmic Auditing; Facebook's **Fairness Flow**.
- Also: codes of ethics for robotics engineers and HRI professionals. Some researchers remain **pessimistic** about machine morality.

---

## 6. Core Ethical Principles

### 6.0 Trust – the foundation
- **Trust** (Lee & See 2004) = attitude that an agent will help achieve one's goals **under uncertainty and vulnerability**.
- Trust drives **user acceptance** – distrusted products fail. Culture matters (e.g. EU cloud customers distrusting the US Patriot Act → data centres moved to Europe after *Safe Harbor* was struck down in 2015).
- Machine trust has **functional** elements (reliability, dependability, false-alarm rate, transparency, task complexity – performance & reliability dominate) and **ethical** elements → the 5 **AI4People** principles (Floridi et al. 2018):

| Principle | Meaning | Examples / notes |
|---|---|---|
| **Non-maleficence** | AI shall **not harm** | Cyber-bullying, **hate speech** (German 2017 law: fines up to €50 M if illegal content isn't removed in a week – but risk of over-removal vs free speech) |
| **Beneficence** | AI shall **do good** (benefits > harms) | Fewer AV accidents, elder care, telemedicine, smart grids, biodiversity, personalised education |
| **Autonomy** | AI shall **respect people's goals & wishes** | Allow informed risk-taking (Everest sherpas); limits – don't help harm others (child says "pull my sister's hair"); Kant's 3 formulations: universal law, humanity as an *end* not *mere means*, kingdom of ends; Asimov's Three Laws ≠ Kantian ethical agent |
| **Justice** | AI shall act **justly and without bias** | → *Bias & Fairness* (6.1) |
| **Explicability** | AI's decisions must be **explainable** | → *Transparency & Explainability* (6.2) |

### 6.1 Bias and Fairness (principle of Justice)

![Fig 4.1 – Justitia](images/fig4.1_justitia.png)

*Fig 4.1 – Justitia: **blindfold** = impartiality, **scales** = weighing evidence, **sword** = punishment.*

- Defining "justice" for a machine is hard because **moral theory is contested**; but in a **narrow scope with clear rules/laws**, AI can make specific moral decisions.
- **Credit scoring:** neighbourhood data → systematic bias against residential areas.
- **Healthcare algorithm (Obermeyer 2019):** race excluded, yet *cost* used as proxy for *need* → poorer (disproportionately Black) patients under-served. Root cause: **problem formulation**.
- **COMPAS (courts):** ProPublica 2016 found bias against African-American defendants in recidivism risk; Northpointe replied about different **base rates**. Chouldechova (2017): **predictive parity and equal false-positive/negative rates can't both hold** when base rates differ → **fairness definitions conflict; fairness–accuracy trade-off**. Accuracy only ≈65% (Dressel & Farid).
- Details of bias types/mitigation → **Unit 2**.

### 6.2 Transparency and Explainability (principle of Explicability)
- **Explicability = intelligibility + accountability** (Floridi). It is **not the same as transparency**: publishing millions of lines of code won't be understood by non-experts and risks competitive secrecy.
- **Intelligibility:** AI is not an inscrutable **black box** – someone can explain it to judges, juries, users.
- **Legal angle:** EU **GDPR "right to information/explanation"** for algorithmic decisions. Challenge for neural networks → research in **Explainable AI (XAI)**.
- **Justification** is part of moral functioning – can't rest on a black box. *Loomis v. Wisconsin:* defendant challenged the proprietary COMPAS score; appeal failed because judges didn't rely on the score alone.
- **Accountability basics:** **log files** (like an aircraft flight recorder / "black box") let investigators retrace steps and assign blame.

### 6.3 Privacy and Security **[+]**
- **Privacy:** control over personal data – AI is data-hungry (Ch. 8 of the book: persistent surveillance, use of data for unintended purposes, auto-insurance discrimination, China's Social Credit System). Principles: **consent, purpose limitation, data minimisation**, anonymisation, GDPR-style rights.
- **Security:** protect data and models from breach, **adversarial attacks**, **data poisoning**, model theft; security failures destroy trust and cause harm (links to non-maleficence).

### 6.4 Robustness and Reliability **[+]**
- **Robustness:** performs correctly under **changed/noisy/adversarial inputs** – the book notes AI **generalises poorly** and lacks common sense (face recogniser fails on profile view).
- **Reliability:** consistent, dependable performance over time; the book says **reliability and performance are the dominant factors in trust**; failures in safety-critical use (autonomous cars, medicine) risk life and injury.
- Practices: stress/edge-case testing, monitoring for drift, fail-safe fallbacks, **human oversight**.

---

## 7. Quick Revision

**One-liners**
- AI = agents that perceive, learn and act to achieve goals; all today's AI is **weak**.
- Ethics: **descriptive** (is) · **normative** (ought) · **meta** (nature of morality) · **applied** (fields).
- Normative: **deontology** (duty/Kant) · **consequentialism** (outcomes/utility) · **virtue** (character/Aristotle).
- Law ≠ ethics but overlap; ethics = **soft law**.
- Machine ethics challenges: no feelings, **no agreed theory**, naive utilities misfire → use **test cases**.
- Five principles: **Non-maleficence, Beneficence, Autonomy, Justice, Explicability**.

**Likely questions**
1. Differentiate strong and weak AI with examples. (2 marks)
2. Explain descriptive, normative and meta-ethics. (6)
3. Compare deontological, consequentialist and virtue ethics using one example. (8)
4. Discuss the relationship between ethics and law. (5)
5. With the toddler–letter example, explain the difficulties in machine ethics. (6)
6. Explain how moral diversity affects testing of ethical AI; name tools for bias testing. (5)
7. Explain the five AI4People principles; relate justice and explicability to COMPAS. (10)
