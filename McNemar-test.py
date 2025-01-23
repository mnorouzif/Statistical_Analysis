from scipy.stats import chi2_contingency

# Define discordant pairs
b = 15  # Misclassified by OKN-MMIC, correctly classified by OKN-MMIC-STEP (FN)
c = 12  # Correctly classified by OKN-MMIC, misclassified by OKN-MMIC-STEP (FP)

# Calculate McNemar's test statistic
mcnemar_statistic = (b - c) ** 2 / (b + c) if (b + c) != 0 else 0

# p-value calculation (1 degree of freedom, chi-squared distribution)
p_value = chi2_contingency([[0, b], [c, 0]])[1]

print(mcnemar_statistic, p_value)
# ====================
# ====================

# Define discordant pairs
b = 15  # Misclassified by OKN-MMIC, correctly classified by OKN-MMIC-STEP (FN)
c = 12  # Correctly classified by OKN-MMIC, misclassified by OKN-MMIC-STEP (FP)

# Calculate McNemar's test statistic
mcnemar_statistic = (b - c) ** 2 / (b + c) if (b + c) != 0 else 0

# p-value calculation (1 degree of freedom, chi-squared distribution)
p_value = chi2_contingency([[0, b], [c, 0]])[1]

print(mcnemar_statistic, p_value)
# ====================
# ====================