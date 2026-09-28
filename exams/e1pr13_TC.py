#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Sep 27 23:02:22 2026

@author: troy
"""

import numpy as np
import sympy as sp
import matplotlib.pyplot as plt

x_pts = np.array([11, 13, 14, 16, 21], dtype=float)
y_pts = x_pts * np.sin(x_pts)

x_sym = sp.Symbol('x')
p_sym = 0
n = len(x_pts)

for i in np.arange(n):
    L_i = 1
    for j in np.arange(n):
        if i != j:
            L_i *= (x_sym - x_pts[j])/(x_pts[i] - x_pts[j])
    p_sym += y_pts[i] * L_i
    
p_sym = sp.simplify(p_sym)
print(p_sym)

p_func = sp.lambdify(x_sym, p_sym, 'numpy')
x_grid = np.linspace(10, 25, 300)

plt.figure(figsize=(8,4))
plt.plot(x_grid, p_func(x_grid), 'c-', label='P(x)')
plt.plot(x_pts, y_pts, 'r*', markersize=12, label='Data Points')
plt.xlim(10,25)
plt.xlabel('x')
plt.ylabel('y')
plt.title('Lecture 3 Handout')
plt.legend()
plt.grid(True)
plt.show()