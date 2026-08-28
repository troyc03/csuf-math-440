import numpy as np

# Coefficients matrix A and right-hand side vector b
A = np.array([
    [4, 1, 1, 0, 1],
    [-1, -3, 1, 1, 0],
    [2, 1, 5, -1, -1],
    [-1, -1, -1, 4, 0],
    [0, 2, -1, 1, 4]
], dtype=float)
b = np.array([6, 6, 6, 6, 6], dtype=float)

# Initial guess starting from x = [0, 0, 0, 0, 0]
x = np.zeros(5)
history = [x.copy()]

# Perform the first 2 iterations
for iteration in range(1, 3):
    x_new = np.zeros(5)
    
    # Jacobi method uses values from the previous iteration 'x'
    x_new[0] = (6 - x[1] - x[2] - x[4]) / 4
    x_new[1] = (6 + x[0] - x[2] - x[3]) / -3
    x_new[2] = (6 - 2*x[0] - x[1] + x[3] + x[4]) / 5
    x_new[3] = (6 + x[0] + x[1] + x[2]) / 4
    x_new[4] = (6 - 2*x[1] + x[2] - x[3]) / 4
    
    x = x_new
    history.append(x.copy())

# Check results
print("History:")
for i, h in enumerate(history):
    print(f"Iter {i}: " + ", ".join([f"{val:.4f}" for val in h]))
