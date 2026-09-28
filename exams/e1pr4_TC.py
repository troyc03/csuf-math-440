#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Sep 27 18:35:14 2026

@author: troy
"""

import numpy as np

A = np.array([
    [2,1,2],
    [1,3,2],
    [2,4,1]
    ]
    )

def power_method(A, tol=1e-6, max_iter=1000):
    x = np.ones(A.shape[0])
    x /= np.linalg.norm(x, np.inf)
    p = np.argmax(np.abs(x))
    
    for k in range(max_iter):
        y = A @ x
        mu = y[p]
        p = np.argmax(np.abs(y))
        
        if y[p] == 0:
            break
        err = np.linalg.norm(x - y/y[p], np.inf)
        
        if err < tol:
            return mu, x, k + 1
        
    return mu, x, max_iter

dom_val, dom_vec, iters_p = power_method(A)

def inv_power_method(A, tol=1e-6, max_iter=1000):
    n = A.shape[0]
    x = np.ones(n)
    q = (x.T @ A @ x)/(x.T @ x)
    p = np.argmax(np.abs(x))
    
    x /= x[p]
    
    for k in range(1, max_iter + 1):
        try: 
            y = np.linalg.solve(A - q * np.eye(n), x)
        except np.linalg.LinAlgError:
            return q, x, k
        
    mu = y[p]
    p = np.argmax(np.abs(y))
    err = np.linalg.norm(x - (y / y[p]), np.inf)
    if err < tol:
        lam = (1.0 / mu) + q
        return lam, x, k
    
    return (1.0 / mu) + q, x, max_iter

small_val, small_vec, iters_inv = inv_power_method(A)

def qr_decomposition(A):
    m, n = A.shape
    Q = np.zeros((m, n))
    R = np.zeros((n, n))
    
    for j in range(n):
        v = A[:, j]
        for i in range(j):
            R[i, j] = np.dot(Q[:, i], A[:, j])
            v = v - R[i, j] * Q[:, i]
        R[j, j] = np.linalg.norm(v)
        Q[:, j] = v/R[j, j]
        
    return Q, R
    
Q, R = qr_decomposition(A)

    