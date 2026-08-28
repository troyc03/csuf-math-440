#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Aug 24 08:44:23 2026

@author: troy
"""

import numpy as np
import matplotlib.pyplot as plt

# 1. Input the given population data
years = np.array([1960, 1970, 1980, 1990, 2000, 2010], dtype=float)
population = np.array([179323, 203302, 226542, 249633, 281442, 307746], dtype=float)
n = len(years)

# 2. Build Newton's divided difference table
# Columns represent F[x_i], F[x_i, x_{i+1}], etc.
table = np.zeros((n, n))
table[:, 0] = population

for j in range(1, n):
    for i in range(n - j):
        table[i, j] = (table[i + 1, j - 1] - table[i, j - 1]) / (years[i + j] - years[i])

# The top row gives the coefficients for the Newton polynomial
coefficients = table[0]

# 3. Define function to evaluate the polynomial at a target year
def evaluate_newton(coef, x_data, x):
    p = coef[-1]
    for k in range(len(coef) - 2, -1, -1):
        p = coef[k] + (x - x_data[k]) * p
    return p

# 4. Predict populations for 1950, 1975, and 2020
target_years = [1950, 1975, 2020]
for year in target_years:
    prediction = evaluate_newton(coefficients, years, year)
    print(f"Population in {year}: {prediction:,.2f} thousand")

# Plot results
target_years = np.array([1950, 1975, 2020], dtype=float)
predictions = np.array([evaluate_newton(coefficients, years, y) for y in target_years])
x_curve = np.linspace(1945, 2025, 200)
y_curve = np.array([evaluate_newton(coefficients, years, x) for x in x_curve])

# 6. Plotting the data, polynomial curve, and estimations
plt.figure(figsize=(10, 6))

# Plot the continuous polynomial line
plt.plot(x_curve, y_curve, color="navy", linestyle="--", label="5th-Degree Interpolating Polynomial")

# Plot original historical data points
plt.scatter(years, population, color="black", zorder=5, label="Given Data (1960 - 2010)")

# Highlight our specific predictions
plt.scatter(target_years, predictions, color="crimson", marker="x", s=100, zorder=6, label="Estimates (1950, 1975, 2020)")

# Annotate the specific estimated points
for y, p in zip(target_years, predictions):
    plt.annotate(f"{y}: {int(round(p)):,}", (y, p), textcoords="offset points", xytext=(0,10), ha='center', color="crimson")

# Chart styling
plt.title("Population Estimates via Newton Divided Difference")
plt.xlabel("Year")
plt.ylabel("Population (thousands)")
plt.legend()
plt.grid(True, linestyle=":", alpha=0.6)

# Display the plot
plt.show()