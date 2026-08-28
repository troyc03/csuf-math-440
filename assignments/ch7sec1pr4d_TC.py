#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Aug 25 21:06:18 2026

@author: troy
"""

import numpy as np

def inf_norm(matrix):
    return max(sum(abs(element) for element in row) for row in matrix)

# Define the matrix
A = np.array([
    [4, -1, 7],
    [-1, 4, 0],
    [-7, 0, 4]
    ])

result = inf_norm(A)
print(f'Infinity Norm: {result}')
