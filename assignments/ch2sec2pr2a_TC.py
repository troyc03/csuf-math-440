#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Aug 22 14:25:14 2026

@author: troy
"""

"""
File name: ch2sec2pr2b_TC.py
Name: Troy Chin
Date: 08-22-2026
"""

def f(x):
    return x**3 - 7*x**2 + 14*x - 6

a, b = 0, 1
tol = 0.01
steps = []
i = 1

# If f(x) = 0 satisfies the IVT, then perform the Bisection Method
while (b - a) / 2 >= tol: 
    m = (a + b) / 2
    fm = f(m)
    steps.append((i, a, b, m, fm, (b-a)/2))
    if fm == 0:
        break
    if f(a) * fm < 0:
        b = m
    else:
        a = m
    i += 1
# Include the final step where the condition is met
m = (a + b) / 2
fm = f(m)
steps.append((i, a, b, m, fm, (b-a)/2))

print("\n     -------- TABLE OF SOLUTIONS TO f(x) = 0 --------   \n")
for s in steps:
    print(f"n={s[0]}: a={s[1]:.4f} | b={s[2]:.4f} | m={s[3]:.4f} | f(m)={s[4]:.4f} | err={s[5]:.4f}")
