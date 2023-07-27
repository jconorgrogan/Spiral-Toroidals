import numpy as np
import sympy as sp
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Define the number of primes to display
num_primes = 900

# Define the function P(n) to get the nth prime number
P = lambda n: sp.prime(n)

# Define the radii for the torus
R = 3
r = 1

# Define the time points
t = np.linspace(0, 2*np.pi, 100)

# Define the parametric equations for the torus
def torus(t, R, r, n):
    theta = t
    phi = P(n) * t
    x = (R + r*np.cos(theta)) * np.cos(phi)
    y = (R + r*np.cos(theta)) * np.sin(phi)
    z = r * np.sin(theta)
    return x, y, z

# Generate the primes
primes = [sp.prime(n) for n in range(1, num_primes + 1)]

# Determine the number of subplot rows and columns
num_cols = 5
num_rows = num_primes // num_cols
if num_primes % num_cols != 0:
    num_rows += 1

# Generate the 3D plots for these primes
fig = plt.figure(figsize=(18, 3.6*num_rows))
for i, p in enumerate(primes):
    ax = fig.add_subplot(num_rows, num_cols, i+1, projection='3d')
    x, y, z = torus(t, R, r, p)
    ax.plot(x, y, z, label=f'Prime {i+1} = {p}')
    ax.set_title(f'Harmonic Oscillation for Prime {i+1} = {p}')
    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_zlabel('Z')
    ax.legend()
plt.tight_layout()
plt.show()
