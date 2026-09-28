#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Sep 27 22:23:54 2026

@author: troy
"""

import numpy as np
import sympy as sp
import matplotlib.pyplot as plt


def symbolic_lagrange(x_data, y_data, x_target):
    y_target = 0.0
    n = len(x_data)
    x_sym = sp.Symbol('x')
    p_sym = 0    
    
    for i in range(n):
        L_i = 1
        for j in range(n):
            if i != j:
                L_i *= (x_sym - x_data[j])/(x_data[i]-x_data[j])
                
        p_sym += y_data[i] * L_i
        
    p_sym = sp.simplify(p_sym)
    target_val = float(p_sym.subs(x_sym, x_target))
    return p_sym, target_val

x_data = np.array([8.1, 8.3, 8.6, 8.7])
y_data = np.array([16.94410, 17.56492, 18.50515, 18.82091])
x_target = 8.4    

p1_sym, p1_val = symbolic_lagrange(x_data[:2], y_data[:2], x_target)
p2_sym, p2_val = symbolic_lagrange(x_data[:3], y_data[:3], x_target)
p3_sym, p3_val = symbolic_lagrange(x_data, y_data, x_target)

print(p1_sym)
print(p1_val)

print(p2_sym)
print(p2_val)

print(p3_sym)
print(p3_val)

x_sym = sp.Symbol('x')
p1_func = sp.lambdify(x_sym, p1_sym, 'numpy')
p2_func = sp.lambdify(x_sym, p2_sym, 'numpy')
p3_func = sp.lambdify(x_sym, p3_sym, 'numpy')
x_grid = np.linspace(8, 8.8, 100)

plt.style.use('dark_background')
plt.figure(figsize=(7, 4))
plt.plot(x_data, y_data, 'ro', label='Data Points')
plt.plot(x_grid, p1_func(x_grid), label='Degree 1 Poly', color='blue')
plt.plot(x_grid, p2_func(x_grid), label='Degree 2 Poly', color='red')
plt.plot(x_grid, p3_func(x_grid), label='Degree 3 Poly', color='green')
plt.title('Lagrange Interpolation')
plt.xlabel('x')
plt.ylabel('y')
plt.legend()
plt.grid(True)
plt.show()