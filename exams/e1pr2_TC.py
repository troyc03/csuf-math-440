#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Sep 27 17:55:45 2026

@author: troy
"""

import numpy as np
import matplotlib.pyplot as plt

x = np.array([1.0, 2.0, 3.0, 4.0, 5.0])
y = np.array([1.3, 3.5, 4.2, 5.0, 7.0])

X = np.column_stack([np.ones_like(x), x])

U, S, Vt = np.linalg.svd(X, full_matrices=False)
S_pinv = np.diag(1.0 / S)
X_pinv = Vt.T @ S_pinv @ U.T
theta_svd = X_pinv @ y

print(f'y = {theta_svd[0]:.2f}+{theta_svd[1]:.2f}*x')

def fit_normal_equation(X, y):
    theta = np.linalg.inv(X.T @ X) @ X.T @ y
    return theta
