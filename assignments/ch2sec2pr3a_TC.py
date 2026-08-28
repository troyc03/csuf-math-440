#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
File name: ch2sec2pr3b_TC.py
Name: Troy Chin
Date: 08-22-2026
"""

def f(x):
    return x**3 - 2*x**2 - 5

# Secant method
p0 = 1.0
p1 = 4.0
tol = 1e-4
max_iter = 20

iterations = []
iterations.append((0, p0, f(p0)))
iterations.append((1, p1, f(p1)))

for i in range(2, max_iter):
    q0 = f(p0)
    q1 = f(p1)
    if abs(q1 - q0) < 1e-15:
        break
    p = p1 - q1 * (p1 - p0) / (q1 - q0)
    iterations.append((i, p, f(p)))
    if abs(p - p1) < tol:
        break
    p0 = p1
    p1 = p

print("\n     -------- TABLE OF SOLUTIONS TO f(x) = 0 --------   \n")
for it in iterations:
    print(f"Iteration {it[0]}: x = {it[1]:.6f} | f(x) = {it[2]:.6f}")


