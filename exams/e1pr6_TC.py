#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Sep 27 19:13:37 2026
@author: troy
"""
import numpy as np

def conjugate_gradient(A, b, x0=None, tol=1e-8, max_iter=100):
    n = len(b)
    if x0 is None:
        x = np.zeros(n)
    else:
        x = x0.copy().astype(float)
        
    r = b - A @ x
    v = r.copy()
    alpha = np.dot(r, r)
    
    for k in range(max_iter):
        if np.linalg.norm(r) < tol:
            return x, r, k
            
        u = A @ v
        t = alpha / np.dot(v, u)
        x += t * v
        r -= t * u
        
        beta = np.dot(r, r)
        if np.sqrt(beta) < tol:
            return x, r, k + 1
            
        s = beta / alpha
        v = r + s * v
        alpha = beta
        
    return x, r, max_iter

A_cg = np.array([
    [4, 3, 0],
    [3, -4, -1],
    [0, -1, 4]
], dtype=float)

b_cg = np.array([24, 30, -24], dtype=float)

sol_cg, res_cg, iters_cg = conjugate_gradient(A_cg, b_cg)
print("Solution:", sol_cg)
print("Iterations:", iters_cg)
