import matplotlib.pyplot as plt
import numpy as np

# Define fault types and their respective fault tolerance levels
faults = ['Chunk Server Down', 'Master Server Overload']
tolerance_original = [20, 40]  # Just indicative percentages for the original system
tolerance_enhanced = [80, 90]  # Hypothetical improvements for the enhanced system

# Define the positions for the groups on the x-axis
x = np.arange(len(faults))  # the label locations
width = 0.35  # the width of the bars, needed to offset bars and prevent overlap

# Create a figure and a set of subplots
fig, ax = plt.subplots()

# Plot the bars for original and enhanced GFS fault tolerance
rects1 = ax.bar(x - width/2, tolerance_original, width, label='Original GFS')
rects2 = ax.bar(x + width/2, tolerance_enhanced, width, label='Enhanced GFS')

# Add some text for labels, title and custom x-axis tick labels, etc.
ax.set_xlabel('Fault Types')
ax.set_ylabel('Fault Tolerance (%)')
ax.set_title('Fault Tolerance Comparison')
ax.set_xticks(x)
ax.set_xticklabels(faults)
ax.legend()

# Attach a text label above each bar in rects1 and rects2, displaying its height.
ax.bar_label(rects1, padding=3)
ax.bar_label(rects2, padding=3)

# Adjust layout to make room for the legend and ensure labels are not cut off
fig.tight_layout()

# Display the plot
plt.show()
