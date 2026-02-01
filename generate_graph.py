import matplotlib.pyplot as plt
import numpy as np

# Data for 2024-2025 Impact Analysis
years = ['2023', '2024', '2025']
global_deaths = [138000, 135000, 128000]  # Global deaths decreasing
project_region_deaths = [1500, 1200, 850] # Sharp decrease in project regions

# Create a figure with two subplots
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(15, 6))

# Plot 1: Global vs Project Region Trends
x = np.arange(len(years))
width = 0.35

rects1 = ax1.bar(x - width/2, global_deaths, width, label='Global Deaths (Est.)', color='#ef4444', alpha=0.7)
rects2 = ax1.bar(x + width/2, [d * 100 for d in project_region_deaths], width, label='Project Area (Scaled x100)', color='#10b981', alpha=0.9)

ax1.set_ylabel('Number of Cases')
ax1.set_title('Mortality Rate Comparison')
ax1.set_xticks(x)
ax1.set_xticklabels(years)
ax1.legend()
ax1.grid(axis='y', alpha=0.3)

# Add summary text
plt.figtext(0.15, 0.02, "Note: Project implementation in 2024 correlates with 29% drop in local mortality.", fontsize=10, style='italic')

# Plot 2: Recovery Rate Improvement
recovery_rates = [75, 88, 96] # Percentage
ax2.plot(years, recovery_rates, marker='o', linewidth=3, color='#3b82f6')
ax2.fill_between(years, recovery_rates, alpha=0.2, color='#3b82f6')
ax2.set_ylim(50, 100)
ax2.set_title('Patient Survival Rate in Analyzed Regions')
ax2.set_ylabel('Survival Rate (%)')
ax2.grid(True, alpha=0.3)

for i, v in enumerate(recovery_rates):
    ax2.text(i, v+1, f"{v}%", ha='center', fontweight='bold')

plt.tight_layout(pad=3.0)

# Save the plot
import os
os.makedirs('demo_images', exist_ok=True)
plt.savefig('demo_images/analysis_graph.png', dpi=100, bbox_inches='tight')
print("Graph generated: demo_images/analysis_graph.png")
