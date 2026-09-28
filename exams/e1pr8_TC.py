#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Sep 27 19:30:43 2026

@author: troy
"""

import numpy as np

def build_system(n):
    dim = n - 1
    A = np.eye(dim)
    for i in range(dim - 1):
        A[i, i+1] = -0.5
        A[i+1, i] = -0.5
    b = np.zeros(dim)
    b[0] = 0.5
    return A, b

def solve_jacobi(A, b, tol=1e-6, max_iter=10000):
    n = len(b)
    x = np.zeros(n)
    D = np.diag(np.diag(A))
    R = A - D
    D_inv = np.diag(1.0 / np.diag(A))
    
    for k in range(max_iter):
        x_new = D_inv @ (b - R @ x)
        if np.linalg.norm(x_new - x, np.inf) < tol:
            return x_new, k + 1
        x = x_new
        
    return x, max_iter

for n in [10, 50, 100]:
    A, b = build_system(n)
    _, iters_j = solve_jacobi(A, b)
    
print(f'n = {n:3d} | Jacobi Iters: {iters_j:5d}')
print('Solutions: \n', solve_jacobi(A, b))