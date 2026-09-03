import numpy as np
import sympy as sp
import matplotlib.pyplot as plt

def lagrange_numeric(x_data, y_data, x_target):
    n = len(x_data)
    y_target = 0.0
    for i in range(n):
        p_i = 1.0
        for j in range(n):
            if i != j:
                p_i *= (x_target - x_data[j]) / (x_data[i] - x_data[j])
        y_target += y_data[i] * p_i
    return y_target

def lagrange_symbolic(x_data, y_data):
    x = sp.Symbol('x')
    poly = 0
    n = len(x_data)
    for i in range(n):
        basis = 1
        for j in range(n):
            if i != j:
                basis *= (x - x_data[j]) / (x_data[i] - x_data[j])
        poly += y_data[i] * basis
    return sp.simplify(poly)

# --- Dataset and Target Definition ---
all_x = np.array([8.1, 8.3, 8.6, 8.7], dtype=float)
all_y = np.array([16.94410, 17.56492, 18.50515, 18.82091], dtype=float)
target_x = 8.4

# Setup for continuous plot lines
x_vals = np.linspace(8.0, 8.8, 200)
x = sp.Symbol('x')

plt.figure(figsize=(10, 6))
plt.scatter(all_x, all_y, color='black', zorder=5, label='Data Points')
plt.axvline(x=target_x, color='gray', linestyle='--', label=f'Target x = {target_x}')

# --- 1. Degree 1 (Linear) ---
# Employs the two points bounding 8.4: 8.3 (index 1) and 8.6 (index 2)
idx_deg1 = [1, 2]
p1 = lagrange_numeric(all_x[idx_deg1], all_y[idx_deg1], target_x)
poly_deg1 = lagrange_symbolic(all_x[idx_deg1], all_y[idx_deg1])
print(f"Degree 1 Approximation at x={target_x}: {p1:.6f}")
print(f"Degree 1 Polynomial: {poly_deg1}\n")

f1 = sp.lambdify(x, poly_deg1, 'numpy')
plt.plot(x_vals, f1(x_vals), label='Degree 1 (Linear)')

# --- 2. Degree 2 (Quadratic) ---
# Employs three closest bounding points: 8.1, 8.3, 8.6
idx_deg2 = [0, 1, 2]
p2 = lagrange_numeric(all_x[idx_deg2], all_y[idx_deg2], target_x)
poly_deg2 = lagrange_symbolic(all_x[idx_deg2], all_y[idx_deg2])
print(f"Degree 2 Approximation at x={target_x}: {p2:.6f}")
print(f"Degree 2 Polynomial: {poly_deg2}\n")

f2 = sp.lambdify(x, poly_deg2, 'numpy')
plt.plot(x_vals, f2(x_vals), label='Degree 2 (Quadratic)')

# --- 3. Degree 3 (Cubic) ---
# Employs all available data points
p3 = lagrange_numeric(all_x, all_y, target_x)
poly_deg3 = lagrange_symbolic(all_x, all_y)
print(f"Degree 3 Approximation at x={target_x}: {p3:.6f}")
print(f"Degree 3 Polynomial: {poly_deg3}\n")