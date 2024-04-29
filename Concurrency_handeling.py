import matplotlib.pyplot as plt
import numpy as np

# Concurrency metrics
metrics = ['Lock Contention', 'Concurrency Throughput']
performance_original = [50, 100]  # Higher contention, lower throughput
performance_enhanced = [10, 200]  # Lower contention, higher throughput

x = np.arange(len(metrics))  # the label locations
width = 0.35  # the width of the bars (Define the width of the bars)

fig, ax = plt.subplots()
rects1 = ax.bar(x - width/2, performance_original, width, label='Original GFS')
rects2 = ax.bar(x + width/2, performance_enhanced, width, label='Enhanced GFS')

ax.set_xlabel('Concurrency Metrics')
ax.set_ylabel('Performance')
ax.set_title('Concurrency Handling Comparison')
ax.set_xticks(x)
ax.set_xticklabels(metrics)
ax.legend()

ax.bar_label(rects1, padding=3)
ax.bar_label(rects2, padding=3)

fig.tight_layout()
plt.show()
