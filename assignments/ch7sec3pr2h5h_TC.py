#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Aug 25 21:18:06 2026

@author: troy
"""

import numpy as np

# Problem 7-2h
def spectral_radius(M):
    # Convert input to a numpy array
    matrix = np.array(M)
    
    # Compute all eigenvalues (NOTE: The spectral radius is the 
    # maximum absolute value of a matrix's set of eigenvalues)
    eigenvalues = np.linalg.eigvals(matrix)
    
    # Return the mnaximum absolute value
    return np.max(np.abs(eigenvalues))

# Define matrix
A = np.array([
    [3, 2, -1],
    [1, -2, 3],
    [2, 0, 4]
    ])

print(f'Spectral Radius: {spectral_radius(A):.2f}')

# Problem 7-5h
l2_norm = np.linalg.norm(A, ord=2)
print(f'L2-Norm: {l2_norm:.2f}')
    
    