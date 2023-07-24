import numpy as np
import matplotlib.pyplot as plt

# List of numbers
numbers = [7]

# Iterate over each number and generate a 2D projection
for num in numbers:
    # Create a new figure and add a subplot
    fig = plt.figure(figsize=(6, 6))
    ax = fig.add_subplot(111)
    ax.set_xlim(-1.5, 1.5)
    ax.set_ylim(-1.5, 1.5)
    ax.set_aspect('equal')
    ax.set_title(f'2D Circle Projection for Number - {num}')

    # Generate points on the circle
    theta = np.linspace(0, 2*np.pi, num, endpoint=False)

    # Draw lines between each pair of points
    for i in range(num):
        for j in range(i+1, num):
            ax.plot([np.cos(theta[i]), np.cos(theta[j])], 
                    [np.sin(theta[i]), np.sin(theta[j])], 
                    '-', linewidth=0.1, color='blue')

    # Save the plot as a high-resolution PNG file
    plt.savefig(f'circle_projection_{num}.png', dpi=1000)
    plt.close()
