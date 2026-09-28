#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Sep 27 22:40:05 2026

@author: troy
"""

import numpy as np

def lagrange_eval(x_nodes, y_nodes, x_eval):
    n = len(x_nodes)
    val = 0.0
    for i in range(n):
        L_i = np.prod([(x_eval - x_nodes[j])/(x_nodes[i]-x_nodes[j]) for j in range(n) if i != j])
        val += y_nodes[i] * L_i      
    return val

nodes = np.array([0.0, 0.6, 0.9])
x_val = 0.45

functions = {
    'a': (np.cos, np.cos(x_val)),
    'b': (lambda x: np.sqrt(1+x), np.sqrt(1+x_val)),
    'c': (lambda x: np.log(x+1), np.log(x_val + 1)),
    'd': (np.tan, np.tan(x_val)) 
    }

for label, (f, true_val) in functions.items():
    p1 = lagrange_eval(nodes[:2], f(nodes[:2]), x_val)
    err1 = abs(true_val - p1)
    
    p2 = lagrange_eval(nodes, f(nodes), x_val)
    err2 = abs(true_val - p2)
    
print(p1); print(err1)
print(p2); print(err2)

