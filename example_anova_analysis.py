"""
Example statistical analysis script
-----------------------------------
Illustrative Python workflow similar to analyses performed for
KALRO-HRI trials (e.g. chicken growth, calf birth weight, bean trials).

This is a demonstrative notebook-style script for the portfolio.
It uses synthetic data that mirrors typical experimental structures
(Completely Randomized or Randomized Complete Block designs).

Author: Joan Achieng Abwao (portfolio example)
"""

import numpy as np
import pandas as pd
from scipy import stats
import statsmodels.api as sm
from statsmodels.formula.api import ols
from statsmodels.stats.anova import anova_lm
from statsmodels.stats.multicomp import pairwise_tukeyhsd

# ------------------------------------------------------------------
# 1. Simulate a simple one-way ANOVA dataset
#    (e.g. three treatments / varieties on a continuous response)
# ------------------------------------------------------------------
np.random.seed(42)

n_per_group = 12
treatments = ["Control", "Biofertilizer A", "Biofertilizer B"]

data = []
means = [18.5, 22.3, 24.1]          # example mean yields or weights
sds   = [2.1, 2.4, 2.0]

for i, (trt, mu, sd) in enumerate(zip(treatments, means, sds)):
    values = np.random.normal(mu, sd, n_per_group)
    for v in values:
        data.append({"treatment": trt, "response": v})

df = pd.DataFrame(data)
print("=== Sample of the data ===")
print(df.groupby("treatment")["response"].describe().round(2))
print()

# ------------------------------------------------------------------
# 2. One-way ANOVA using statsmodels (OLS)
# ------------------------------------------------------------------
model = ols("response ~ C(treatment)", data=df).fit()
anova_table = anova_lm(model, typ=2)

print("=== ANOVA Table ===")
print(anova_table.round(4))
print()

# ------------------------------------------------------------------
# 3. Post-hoc pairwise comparisons (Tukey HSD)
# ------------------------------------------------------------------
tukey = pairwise_tukeyhsd(endog=df["response"],
                          groups=df["treatment"],
                          alpha=0.05)
print("=== Tukey HSD Post-hoc ===")
print(tukey)
print()

# ------------------------------------------------------------------
# 4. Alternative: classic scipy one-way ANOVA
# ------------------------------------------------------------------
groups = [df.loc[df.treatment == t, "response"].values for t in treatments]
f_stat, p_val = stats.f_oneway(*groups)
print(f"SciPy one-way ANOVA: F = {f_stat:.3f}, p = {p_val:.4f}")

# ------------------------------------------------------------------
# Notes for real analyses at KALRO-HRI
# ------------------------------------------------------------------
# • For RCBD / blocked designs include the block factor:
#       model = ols("response ~ C(treatment) + C(block)", data=df).fit()
# • For mixed / repeated measures use MixedLM or lmer-style models.
# • Always check residual normality (Shapiro-Wilk) and homogeneity
#   of variance (Levene / Bartlett) before interpreting ANOVA.
# • For binary outcomes (KAP surveys) use logistic regression:
#       logit_model = sm.Logit(y, X).fit()
