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
