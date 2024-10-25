import matplotlib.pyplot as plt
import numpy as np

# Distance from Chennai to Bangalore (approx in miles)
distance = 200  # Example distance

# Convert degrees to radians
def deg_to_rad(degrees):
    return degrees * (np.pi / 180)

# Initial course angle (let's assume the angle is 0 degrees for a straight line)
initial_angle = 0  # heading towards Bangalore

# New course angle with a 1% deviation
deviation_angle = deg_to_rad(0.01)  # 1% deviation

# X and Y coordinates for the original course (straight line)
x_orig = np.array([0, distance * np.cos(initial_angle)])
y_orig = np.array([0, distance * np.sin(initial_angle)])

# X and Y coordinates for the deviated course
x_dev = np.array([0, distance * np.cos(initial_angle + deviation_angle)])
y_dev = np.array([0, distance * np.sin(initial_angle + deviation_angle)])

# Plot the original and deviated courses
plt.figure(figsize=(8, 6))
plt.plot(x_orig, y_orig, label="Original Course", color="blue", marker='o')
plt.plot(x_dev, y_dev, label="Deviated Course (1% change)", color="red", marker='x')

# Add labels, title, and legend
plt.title('Effect of 1% Change in Direction on Course')
plt.xlabel('Distance (miles)')
plt.ylabel('Deviation (miles)')
plt.legend()
plt.grid(True)

# Highlight the deviation point after a distance of 200 miles
deviation_distance = np.sqrt((x_dev[1] - x_orig[1])**2 + (y_dev[1] - y_orig[1])**2)
plt.text(0, -5, f'Deviation: {deviation_distance:.2f} miles', fontsize=12, color='red')

# Show the plot
plt.show()
