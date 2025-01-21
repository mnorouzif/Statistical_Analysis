import matplotlib.pyplot as plt
import numpy as np

# Data for visualization
methods = ['OKN-MMIC', 'OKN-MMIC-STEP']
true_positives = [305, 310]
false_negatives = [15, 10]
false_positives = [12, 15]
true_negatives = [142, 139]

# Bar chart for comparison
x = np.arange(len(methods))
bar_width = 0.2

fig, ax = plt.subplots(figsize=(10, 6))

# Bars for each metric
tp_bar = ax.bar(x - bar_width, true_positives, bar_width, label='True Positives', color='green')
fn_bar = ax.bar(x, false_negatives, bar_width, label='False Negatives', color='red')
fp_bar = ax.bar(x + bar_width, false_positives, bar_width, label='False Positives', color='orange')
tn_bar = ax.bar(x + 2 * bar_width, true_negatives, bar_width, label='True Negatives', color='blue')

# Add labels and titles
ax.set_xlabel('Models', fontsize=12)
ax.set_ylabel('Counts', fontsize=12)
ax.set_title('Comparison of Metrics Between OKN-MMIC and OKN-MMIC-STEP', fontsize=14)
ax.set_xticks(x + bar_width / 2)
ax.set_xticklabels(methods, fontsize=12)
ax.legend()

# Add value labels to bars
for bar_group in [tp_bar, fn_bar, fp_bar, tn_bar]:
    for bar in bar_group:
        yval = bar.get_height()
        ax.text(bar.get_x() + bar.get_width() / 2, yval + 1, int(yval), ha='center', fontsize=10)

plt.tight_layout()
plt.show()
