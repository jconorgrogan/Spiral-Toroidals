import numpy as np
import matplotlib.pyplot as plt
from matplotlib.collections import LineCollection
from matplotlib import cm
from matplotlib.animation import FuncAnimation, PillowWriter

# Initialize parameters
num = 80  # Number of nodes
theta = np.linspace(0, 2*np.pi, num, endpoint=False)
standing_amplitude = 0.2
standing_wave = standing_amplitude * np.sin(3 * theta)
perturbation_amplitude = 0.2
perturbation_width = np.pi / 8

# Calculate perturbation with reverberations
def calculate_reverberating_perturbation(theta, perturbation_center):
    primary = perturbation_amplitude * np.sin(5 * theta) * np.exp(-(theta - perturbation_center)**2 / (2 * perturbation_width**2))
    rev1 = 0.1 * perturbation_amplitude * np.sin(5 * theta) * np.exp(-((theta - perturbation_center) - np.pi/8)**2 / (2 * perturbation_width**2))
    rev2 = 0.05 * perturbation_amplitude * np.sin(5 * theta) * np.exp(-((theta - perturbation_center) - np.pi/4)**2 / (2 * perturbation_width**2))
    return primary + rev1 + rev2

# Function to update the figure for each frame of the animation
def update_animation(perturbation_center):
    ax.clear()
    ax.set_xlim(-1.5, 1.5)
    ax.set_ylim(-1.5, 1.5)
    ax.set_aspect('equal')
    
    perturbation = calculate_reverberating_perturbation(theta, perturbation_center)
    first_harmonic = 0.05 * np.sin(2 * theta)
    second_harmonic = 0.03 * np.sin(4 * theta)
    harmonic_wave = perturbation + first_harmonic + second_harmonic
    combined_wave = 1.0 + 0.05 * standing_wave + harmonic_wave
    x_nodes = combined_wave * np.cos(theta)
    y_nodes = combined_wave * np.sin(theta)
    
    lines = []
    color_values = []
    for i in range(num):
        for j in range(i+1, num):
            lines.append([(x_nodes[i], y_nodes[i]), (x_nodes[j], y_nodes[j])])
            distance = np.sqrt((x_nodes[i] - x_nodes[j])**2 + (y_nodes[i] - y_nodes[j])**2)
            color_values.append(distance)
    
    line_collection = LineCollection(lines, array=np.array(color_values), cmap=cm.viridis, linewidths=0.5)
    ax.add_collection(line_collection)
    ax.scatter(x_nodes, y_nodes, c=combined_wave, cmap=cm.viridis, s=10)

# Set up the figure and animation
fig, ax = plt.subplots(figsize=(10, 10))
ani = FuncAnimation(fig, update_animation, frames=np.linspace(0, 2*np.pi, 30), repeat=True)

# Save the animation as a movie (e.g., mp4 format). Ensure you have the appropriate writer (e.g., ffmpeg) installed.
# ani.save('torus_perturbation_movie.mp4', writer='ffmpeg', fps=10)

# Uncomment the save line and execute the code to generate the movie on your local setup.
