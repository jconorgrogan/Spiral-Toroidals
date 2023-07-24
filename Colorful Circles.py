import numpy as np
import matplotlib.pyplot as plt
import math
from matplotlib import cm

# List of numbers
numbers = [80,81,82,83,84]

# Create a new figure
fig, axs = plt.subplots(nrows=1, ncols=len(numbers), figsize=(6 * len(numbers), 6))
plt.tight_layout(pad=3.0)

# Iterate over each number and generate a 2D projection
for ax, num in zip(axs, numbers):
    # Set plot limits and aspect ratio
    ax.set_xlim(-1.5, 1.5)
    ax.set_ylim(-1.5, 1.5)
    ax.set_aspect('equal')
    ax.set_title(f'2D Circle Projection for Number - {num}')

    # Generate points on the circle
    theta = np.linspace(0, 2*np.pi, num, endpoint=False)

    # Calculate the slopes of the lines for intersections
    slopes = {}
    for i in range(num):
        for j in range(i+1, num):
            # Calculate the slope of the line
            slope = (np.sin(theta[j]) - np.sin(theta[i])) / (np.cos(theta[j]) - np.cos(theta[i]))
            if math.isinf(slope):
                slope = float('inf')

            # Round the slope to a certain number of decimal places to avoid float precision issues
            slope = round(slope, 3)

            if slope not in slopes:
                slopes[slope] = len(slopes)

            # Draw line between each pair of points
            ax.plot([np.cos(theta[i]), np.cos(theta[j])],
                    [np.sin(theta[i]), np.sin(theta[j])],
                    '-', linewidth=0.1, color=cm.viridis(slopes[slope] / num))

    # Print the counts of unique circles
    print(f'Number - {num} | Unique circles - {len(slopes)}')

# Save the entire figure as a high-resolution PNG file
plt.savefig('circle_projections.png', dpi=1000)
plt.close()
