#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Sep 27 18:55:53 2026
@author: troy
"""
import numpy as np

def householder_tridiagonal(A_input):
    A = A_input.copy().astype(float)
    n = A.shape[0]
    
    for k in range(n - 2):
        q = np.sum(A[k+1:, k]**2)
        if q == 0:
            continue  # Already tridiagonalized for this column
            
        if A[k+1, k] == 0:
            alpha = -np.sqrt(q)
        else:
            alpha = -np.sqrt(q) * A[k+1, k] / abs(A[k+1, k])
            
        RSQ = alpha ** 2 - alpha * A[k+1, k]
        
        v = np.zeros(n)
        v[k+1] = A[k+1, k] - alpha
        v[k+2:] = A[k+2:, k]
        
        u = (1.0 / RSQ) * (A[k+1:, k+1:] @ v[k+1:])
        u_full = np.zeros(n)
        u_full[k+1:] = u
        
        PROD = np.dot(v[k+1:], u_full[k+1:])
        
        z = u_full - (PROD / (2 * RSQ)) * v
        
        for i in range(k + 1, n):
            for j in range(k + 1, n):
                A[i, j] -= (v[i] * z[j] + z[i] * v[j])
               
        for j in range(k + 2, n):
            A[k, j] = 0.0
            A[j, k] = 0.0
        A[k+1, k] = alpha
        A[k, k+1] = alpha
        
    return A

A = np.array([[4, -1, -1, 0],[-1, 4, 0, 1],[-1, 0, 4, -1],[0, -1, -1, 4]])
print(householder_tridiagonal(A))