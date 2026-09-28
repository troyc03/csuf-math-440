#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Sep 27 19:25:40 2026

@author: troy
"""

import numpy as np

def sor(A, b, omega=1.1):
    n = len(b)
    x = np.zeros(n)
    
    for k in range(1, 3):
        x_new = x.copy()
        for i in range(n):
            sum1 = sum(A[i, j] * x_new[j] for j in range(i))
            sum2 = sum(A[i, j] * x[j] for j in range(i + 1, n))
            x_new[i] = (1 - omega) * x[i] + (omega / A[i, i]) * (b[i] - sum1 - sum2)
        x = x_new
    return x

A_a = np.array([
    [3, -1, 1],
    [3, 6, 2],
    [3, 3, 7]
    ], dtype=float)
b_a = np.array([1, 0, 4], dtype=float)

print(sor(A_a, b_a, omega=1.1))

