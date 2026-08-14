import matplotlib.pyplot as plt
import numpy as np

# 1. Setup parameters
n_steps = 1000  # Total iterations
n_visual = 100  # Number of points to plot at the end
n_r = 2000  # Resolution of the r axis

# 2. Initialize arrays
r = np.linspace(2.5, 4.0, n_r)
x = 0.5 * np.ones(n_r)

# 3. Vectorized simulation
plt.figure(figsize=(10, 7))

for step in range(n_steps):
    # Vectorized update rule
    x = r * x * (1 - x)

    # Plot the final stable points
    if step >= (n_steps - n_visual):
        plt.plot(r, x, ",k", alpha=0.25)

# 4. Finalize plot
plt.title("Feigenbaum Bifurcation Diagram (Logistic Map)")
plt.xlabel("Growth Rate (r)")
plt.ylabel("Equilibrium State (x)")
plt.show()
