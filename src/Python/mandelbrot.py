import numpy as np
import matplotlib.pyplot as plt

def compute_mandelbrot(N, max_iters=100):
    """Computes the Mandelbrot set grid.

    Returns a 2D array containing the number of iterations reached before
    escaping, or max_iters if it stays bounded.
    """
    # Create an N x N grid spanning -2 to 2 for both real (x) and imaginary (y) parts
    x = np.linspace(-2, 2, N)
    y = np.linspace(-2, 2, N)

    # Combine x and y into a 2D grid of complex constants c
    X, Y = np.meshgrid(x, y)
    C = X + 1j * Y

    # Initialize z to 0 (same shape as C) and iteration counts to 0
    Z = np.zeros_like(C)
    iterations = np.zeros(C.shape, dtype=int)

    # Perform the iteration z' = z^2 + c
    for i in range(max_iters):
        # Create a mask of points that have not yet escaped (|z| <= 2)
        not_escaped = np.abs(Z) <= 2

        # Only update points that haven't escaped yet
        Z[not_escaped] = Z[not_escaped] ** 2 + C[not_escaped]
        iterations[not_escaped] = i

    return iterations


# --- Configuration ---
N = 1000  # Grid size (use N=100 for fast testing, N=1000 for high quality)
max_iters = 100  # Maximum number of iterations

# Compute the dataset
grid_data = compute_mandelbrot(N, max_iters)

# --- Plot 1: Standard Black & White ---
# Points inside the set (hit max_iters) are black (0), points outside are white (1)
bw_grid = np.where(grid_data == max_iters - 1, 0, 1)

plt.figure(figsize=(6, 6))
plt.imshow(
    bw_grid, cmap="gray", extent=[-2, 2, -2, 2], origin="lower"
)
plt.title("Mandelbrot Set (Black & White)")
plt.xlabel("Re(c)")
plt.ylabel("Im(c)")
plt.show()

# --- Plot 2: Colorful Variation (Logarithmic Scale) ---
# Using the 'hot' colormap and log scale to highlight fine structures
log_grid = np.log(grid_data + 1)

plt.figure(figsize=(7, 6))
plt.imshow(
    log_grid, cmap="hot", extent=[-2, 2, -2, 2], origin="lower"
)
plt.colorbar(label="Log(Iterations to Escape)")
plt.title("Mandelbrot Set (Colorful Log Scale)")
plt.xlabel("Re(c)")
plt.ylabel("Im(c)")
plt.show()
