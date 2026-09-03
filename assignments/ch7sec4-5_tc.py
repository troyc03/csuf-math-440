#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Name: Troy Chin
"""

import numpy as np

w_0 = 1.2
x1, x2, x3, x4 = 0,0,0,0
x_old = np.array([x1, x2, x3, x4])
eps = 1e-6
converged = False

# Gauss-Seidel algorithm
print('\n------- Gauss Seidel Method -------')
for k in range(1, 6): 
    x1 = (x2-2*x3+6)/10
    x2 = (x1+x3+25)/11
    x3 = (2*x1+x2+x4-11)/10
    x4 = (-3*x2+x3+15)/8
    x = np.array([x1,x2,x3,x4])
    dx = np.sqrt(np.dot(x-x_old, x-x_old))
    
    print(f'{k} | {x1:.4f} | {x2:.4f} | {x3:.4f} | {x4:.4f}')
    
    if dx < eps:
        converged = True
        break
    
    x_old = x

x_old = np.array([0, 0, 0, 0], dtype=float)
converged = False

print('\n------- Jacobi Method -------')
# Jacobi Method
for k in range(1, 6):
    # Calculations strictly use elements from the previous iteration vector (x_old)
    x1_new = (x_old[1] - 2 * x_old[2] + 6) / 10
    x2_new = (x_old[0] + x_old[2] + 25) / 11
    x3_new = (2 * x_old[0] + x_old[1] + x_old[3] - 11) / 10
    x4_new = (-3 * x_old[1] + x_old[2] + 15) / 8
    
    x = np.array([x1_new, x2_new, x3_new, x4_new])
    dx = np.sqrt(np.dot(x - x_old, x - x_old))
    print(f'{k} | {x[0]:.4f} | {x[1]:.4f} | {x[2]:.4f} | {x[3]:.4f}')
    
    if dx < eps:
        converged = True
        break
    x_old = x

x1, x2, x3, x4 = 0, 0, 0, 0
x_old = np.array([x1, x2, x3, x4], dtype=float)
converged = False

print('\n------- SOR Method -------')
for k in range(1, 6):
    x1_gs = (x2 - 2*x3 + 6) / 10
    x1 = (1 - w_0) * x_old[0] + w_0 * x1_gs
    x2_gs = (x1 + x3 + 25) / 11
    x2 = (1 - w_0) * x_old[1] + w_0 * x2_gs
    x3_gs = (2*x1 + x2 + x4 - 11) / 10
    x3 = (1 - w_0) * x_old[2] + w_0 * x3_gs
    x4_gs = (-3*x2 + x3 + 15) / 8
    x4 = (1 - w_0) * x_old[3] + w_0 * x4_gs
    x = np.array([x1, x2, x3, x4])
    dx = np.sqrt(np.dot(x - x_old, x - x_old))
    print(f'{k} | {x1:.4f} | {x2:.4f} | {x3:.4f} | {x4:.4f}')
    
    if dx < eps:
        converged = True
        break
    x_old = x
