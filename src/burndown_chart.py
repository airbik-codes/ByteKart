import matplotlib.pyplot as plt

# Data for burndown chart
weeks = ['Week 1', 'Week 2', 'Week 3', 'Week 4', 'Week 5', 'Week 6', 'Week 7', 'Week 8']
work_remaining = [100, 90, 75, 65, 50, 40, 25, 10]  # Remaining work (in story points)

# Create the plot
plt.plot(weeks, work_remaining, marker='o', linestyle='-', color='blue', label='Work Remaining')

# Customize the plot
plt.title('Sprint Burndown Chart')
plt.xlabel('Week')
plt.ylabel('Work Remaining (Story Points)')
plt.grid(True)
plt.xticks(rotation=45)
plt.tight_layout()

# Save the chart as a PNG image
plt.savefig('burndown_chart.png')

# Show the chart
plt.show()
