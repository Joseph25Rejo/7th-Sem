"""Unit-2 demo: detect and mitigate bias in a loan-approval classifier.

Uses only numpy, pandas and scikit-learn. The data is synthetic: historical
approvals were biased against group B, so a model trained on it inherits the bias.
Run:  python bias_detection_demo.py
"""
import numpy as np
import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split

rng = np.random.default_rng(0)
n = 8000
group = rng.choice(["A", "B"], size=n, p=[0.6, 0.4])             # protected attribute
skill = rng.normal(0, 1, n)                                       # true merit (same in both groups)
zip_score = np.where(group == "A", 1.0, -1.0) + rng.normal(0, 0.7, n)   # proxy for group
deserves = (skill > 0.3).astype(int)                              # ground truth "qualified"
# Biased historical decisions: group B needed much higher merit to be approved.
approved = (skill - np.where(group == "B", 0.9, 0.0) + rng.normal(0, 0.4, n) > 0.3).astype(int)

df = pd.DataFrame({"group": group, "skill": skill, "zip_score": zip_score,
                   "approved": approved, "deserves": deserves})
X = df[["skill", "zip_score"]]         # protected attribute NOT used, but zip_score is a proxy
X_tr, X_te, y_tr, y_te, g_tr, g_te, _, d_te = train_test_split(
    X, df["approved"], df["group"], df["deserves"], test_size=0.3, random_state=1)


def report(y_pred, g, title, y_true=d_te):
    print(f"\n== {title}")
    rows = {}
    for grp in ["A", "B"]:
        m = (g == grp).to_numpy()
        yt, yp = y_true.to_numpy()[m], y_pred[m]
        rows[grp] = {
            "selection_rate": yp.mean(),
            "TPR (qualified approved)": yp[yt == 1].mean(),
            "FPR (unqualified approved)": yp[yt == 0].mean(),
        }
    print(pd.DataFrame(rows).T.round(3))
    sr = {k: v["selection_rate"] for k, v in rows.items()}
    print("Statistical parity difference (B - A):", round(sr["B"] - sr["A"], 3))
    print("Disparate impact ratio (B / A):      ", round(sr["B"] / sr["A"], 3), "(< 0.8 fails the 80% rule)")
    print("Equal-opportunity difference (TPR B - A):", round(rows["B"]["TPR (qualified approved)"] - rows["A"]["TPR (qualified approved)"], 3))


# 1. Detect: baseline model
model = LogisticRegression(max_iter=1000).fit(X_tr, y_tr)
report(model.predict(X_te), g_te, "Baseline model (bias detected)")

# 2. Mitigate (pre-processing): reweighing so group and label become independent
w = np.ones(len(y_tr))
for grp in ["A", "B"]:
    for lab in [0, 1]:
        m = ((g_tr == grp) & (y_tr == lab)).to_numpy()
        expected = (g_tr == grp).mean() * (y_tr == lab).mean()
        w[m] = expected / m.mean()
rw = LogisticRegression(max_iter=1000).fit(X_tr, y_tr, sample_weight=w)
report(rw.predict(X_te), g_te, "After reweighing (pre-processing)")

# 3. Mitigate (post-processing): group-specific thresholds to equalise selection rate
p = model.predict_proba(X_te)[:, 1]
target = (p[(g_te == "A").to_numpy()] > 0.5).mean()
thr_B = np.quantile(p[(g_te == "B").to_numpy()], 1 - target)
pred = np.where((g_te == "B").to_numpy(), p > thr_B, p > 0.5).astype(int)
report(pred, g_te, "After threshold adjustment (post-processing)")
