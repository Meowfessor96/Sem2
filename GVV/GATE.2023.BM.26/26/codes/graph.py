import matplotlib.pyplot as plt
import numpy as np

# Load the data from data.dat, skipping the first row
data = np.loadtxt("data.dat", skiprows=1)

# Extracting n and y values
n_values = np.arange(10)
y_values = np.where(n_values == 0, 1, 0.5**n_values)

# Create a stem plot without highlighting
plt.stem(n_values, y_values, linefmt='b-', markerfmt='bo', basefmt='b-', label='Stem Plot')

plt.xlabel('n')
plt.ylabel('h[n]')
plt.grid(True)
plt.legend()

plt.savefig('../figs/fig1.png')
