#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Aug 24 08:08:53 2026

@author: troy
"""
 
import numpy as np

def lagrange(x_data, y_data, x_target):
    n = len(x_data) # Number of nodes
    y_target = 0.0 # Target data
    
    for i in range(n):
        # Calculate basis polynomial P_i(x_target)
        p_i = 1.0
        for j in range(n):
            if i != j:
                p_i *= (x_target - x_data[j]) / (x_data[i] - x_data[j])
    # Add the weighted term to the final sum
    y_target += y_data[i] * p_i
    
    return y_target

# Complete dataset provided in the problem
all_x = np.array([8.1, 8.3, 8.6, 8.7], dtype=float)
all_y = np.array([16.94410, 17.56492, 18.50515, 18.82091], dtype=float)
target_x = 8.4

# --- 1. Degree 1 (Linear) ---
# Uses the two closest points bounding 8.4: index 1 (8.3) and index 2 (8.6)
idx_deg1 = [1, 2]
p1 = lagrange(all_x[idx_deg1], all_y[idx_deg1], target_x)
print(f"Degree 1 (Points: {all_x[idx_deg1]}): {p1:.6f}")

# --- 2. Degree 2 (Quadratic) ---
# Uses the three closest points: index 0 (8.1), index 1 (8.3), and index 2 (8.6)
idx_deg2 = [0, 1, 2]
p2 = lagrange(all_x[idx_deg2], all_y[idx_deg2], target_x)
print(f"Degree 2 (Points: {all_x[idx_deg2]}): {p2:.6f}")

# --- 3. Degree 3 (Cubic) ---
# Uses all four data points
p3 = lagrange(all_x, all_y, target_x)
print(f"Degree 3 (Points: {all_x}): {p3:.6f}")