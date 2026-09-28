#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Sep 27 22:54:29 2026

@author: troy
"""

import numpy as np
import matplotlib.pyplot as plt

def lagrange_eval(x_nodes, y_nodes, x_eval):
    n = len(x_nodes)
    val = 0.0
    for i in range(n):
        L_i = np.prod([(x_eval - x_nodes[j])/(x_nodes[i]-x_nodes[j]) for j in range(n) if i != j])
        val += y_nodes[i] * L_i      
    return val

years = np.array([1960, 1970, 1980, 1990, 2000, 2010], dtype=float)
pop = np.array([179323, 203302, 226542, 249633, 281442, 307746], dtype=float)

sel_idx = [0, 2, 5]
x_sel = years[sel_idx]
y_sel = pop[sel_idx]

eval_years = [1950, 1975, 2020]
eval_pops = [lagrange_eval(x_sel, y_sel, yr) for yr in eval_years]

for yr, p in zip(eval_years, eval_pops):
    print(f'Estimated population in {yr}: {p:.2f} thousand')
    
grid_years = np.linspace(1945, 2025, 200)
grid_pops = [lagrange_eval(x_sel, y_sel, yr) for yr in grid_years]

plt.style.use('dark_background')
plt.figure(figsize=(8,4))
plt.plot(grid_years, grid_pops, 'b-', label='Interpolating Line of Best Fit')
plt.plot(years, pop, 'ko', label='Original Data')
plt.plot(eval_years, eval_pops, 'r*', markersize=10, label='Evaluated Points')
plt.xlabel('Year')
plt.ylabel('Population')
plt.title('Population Data')
plt.legend()
plt.grid(True)
plt.show()
