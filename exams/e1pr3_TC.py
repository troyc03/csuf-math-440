#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Sep 27 18:17:25 2026

@author: troy
"""

import numpy as np

def analyze_system(A, b, system_type):
    Q, R = np.linalg.qr(A)
    U, S, Vt = np.linalg.svd(A)
    
    x_ls = np.linalg.pinv(A) @ b
    res = np.linalg.norm(A @ x_ls - b, ord=2)
    
    return A, b, S, x_ls, res

"""
# Test Case
analyze_system(A_a, b_a, 'a) Unique Solution')
Out[36]: 
(array([[2., 1.],
        [1., 3.]]),
 array([5., 6.]),
 array([3.61803399, 1.38196601]),
 array([1.8, 1.4]),
 np.float64(2.5121479338940403e-15))

 analyze_system(A_a, b_a, '(b) Infinite Solutions')
Out[39]: 
(array([[1., 2., 3.],
        [2., 4., 6.]]),
 array([ 6., 12.]),
 array([8.36660027e+00, 5.61733355e-16]),
 array([0.42857143, 0.85714286, 1.28571429]),
 np.float64(1.9860273225978185e-15))

A_a = np.array([[1, 2] [2, 4], [3,6], dtype=float)

analyze_system(A_a, b_a, '(c) Inconsistent')
Out[45]: 
(array([[1., 2.],
        [2., 4.],
        [3., 6.]]),
 array([1., 1., 4.]),
 array([8.36660027e+00, 4.44089210e-16]),
 array([0.21428571, 0.42857143]),
 
 analyze_system(A_a, b_a, '(d) Inconsistent')
 Out[48]: 
 (array([[1., 2.],
         [2., 4.],
         [3., 6.]]),
  array([1., 1., 1.]),
  array([8.36660027e+00, 4.44089210e-16]),
  array([0.08571429, 0.17142857]),
  np.float64(0.6546536707079772))
"""