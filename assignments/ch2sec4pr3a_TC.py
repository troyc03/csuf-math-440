#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Aug 24 10:47:39 2026

@author: troy
"""

def f(x):
    return x**3 - 2*x**2 - 5

def df(x):
    return 3*x**2 - 4*x

def newton_method(x0, tol=1e-4, max_iter=100):
    x = x0
    print(f"{'Iter':<5}{'x_n':<12}{'x_next':<12}{'Difference':<12}")
    print("-" * 45)
    
    for i in range(max_iter):
        fx = f(x)
        dfx = df(x)
        
        if dfx == 0:
            print("Derivative is zero. Method failed.")
            return None
            
        x_next = x - fx / dfx
        diff = abs(x_next - x)
        
        print(f"{i+1:<5}{x:<12.6f}{x_next:<12.6f}{diff:<12.6e}")
        
        if diff < tol:
            return x_next
        x = x_next
        
    print("Maximum iterations reached without convergence.")
    return None

# Execution
root = newton_method(x0=2.5)
print(f"\nApproximate root: {root:.4f}")
