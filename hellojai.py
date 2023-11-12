import matplotlib.pyplot as plt
import numpy as np

# Generate sample data
x = np.random.normal(0, 1, 100)  # Random data for scatter plot
labels = ['A', 'B', 'C', 'D']
sizes = [15, 30, 45, 10]  # Sizes for the pie chart
data = [np.random.normal(0, 1, 100) for _ in range(4)]  # Data for box plot

# Create a figure with multiple subplots
plt.figure(figsize=(12, 4))

# Plot the first graph (Scatter Plot)
plt.subplot(1, 3, 1)
plt.scatter(range(len(x)), x, marker='o', c='blue', alpha=0.7)
plt.title('Scatter Plot')

# Plot the second graph (Pie Chart)
plt.subplot(1, 3, 2)
plt.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=140)
plt.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
plt.title('Pie Chart')

# Plot the third graph (Box Plot)
plt.subplot(1, 3, 3)
plt.boxplot(data, labels=labels)
plt.title('Box Plot')

# Show the plots
plt.tight_layout()
plt.show()
