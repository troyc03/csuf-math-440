# -*- coding: utf-8 -*-
"""Lecture 1 Handout: Numerical Root-Finding Methods"""

# Define the function and its derivative
f = lambda x: x**3 + 4*x**2 - 10
df = lambda x: 3*x**2 + 8*x

# 1. Bisection Method
def bisection(f, a, b, tol=1e-6, max_iter=100):
    if f(a) * f(b) >= 0:
      raise ValueError("Bisection fail: function must have opposite signs at endpoints.")
    for i in range(max_iter):
      c = (a + b) / 2.0
      fc = f(c)
      if abs(fc) < tol or (b - a) / 2.0 < tol:
        return c, i
      if f(a) * fc < 0:
        b = c
      else:
        a = c
    raise ValueError("Maximum iterations reached without convergence.")

# 2. Newton-Raphson Method
def newton(f, df, x0, tol=1e-6, max_iter=100):
    x = x0
    for i in range(max_iter):
      fx = f(x)
      if abs(fx) < tol:
        return x, i
      dfx = df(x)
      if dfx == 0:
        raise ValueError("Derivative error. No convergence.")
      x = x - fx / dfx
    raise ValueError("Maximum iterations reached without convergence.")

# 3. Secant Method
def secant(f, x0, x1, tol=1e-6, max_iter=100):
    for i in range(max_iter):
      fx0 = f(x0)
      fx1 = f(x1)
      if abs(fx1) < tol:
        return x1, i
      if fx1 - fx0 == 0:
        raise ValueError("Division by zero in secant method.")
      x2 = x1 - fx1 * (x1 - x0) / (fx1 - fx0)
      if abs(x2 - x1) < tol:
        return x2, i + 1
      x0, x1 = x1, x2
    raise ValueError("Maximum iterations reached without convergence.")

# Test and print results
root_bis, iter_bis = bisection(f, 1, 2)
root_newton, iter_newton = newton(f, df, 1)
root_sec, iter_sec = secant(f, 1, 2)

print('\n=========== SOLUTIONS TO f(x) = 0 ===========\n')
print(f"Bisection Root: {root_bis:.8f} | Iterations: {iter_bis}")
print(f"Newton Root:    {root_newton:.8f} | Iterations: {iter_newton}")
print(f"Secant Root:    {root_sec:.8f} | Iterations: {iter_sec}")
