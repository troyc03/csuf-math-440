#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Sep 27 22:07:01 2026

@author: troy
"""

import numpy as np

def compute_eigen_and_norms(M, label):
    vals, vecs = np.linalg.eig(M)    
    norm_l2 = np.linalg.norm(M, 2)
    norm_linf = np.max(np.sum(np.abs(M), axis=1))
    
    return vals, vecs, norm_l2, norm_linf

matrices = {
    'a': np.array([[2, -1], [-1, 2]], dtype=float),
    'b': np.array([[0, 1], [1, 1]], dtype=float),
    'c': np.array([[0, 0.5], [0.5, 0]], dtype=float),
    'd': np.array([[1,1], [-2,-2]], dtype=float)    
    }

for name, M in matrices.items():
    compute_eigen_and_norms(M, name)

print(compute_eigen_and_norms(M, name))    