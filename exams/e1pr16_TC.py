import numpy as np

def f(w):
    return ((g/2)*w**2) * ((np.exp(w) - np.exp(-w))/2.0*np.sin(w)- target_x)

def df(w):
    h = 1e-7
    return (f(w + h) - f(w - h)) / (2 * h)

def bisection(a, b, tol=1e-5):
    if f(a) * f(b) >= 0:
        raise ValueError("f(a) and f(b) must have opposite signs.")
    while (b - a) / 2.0 > tol:
        m = (a + b) / 2.0
        if f(m) == 0:
            return m
        elif f(a) * f(m) < 0:
            b = m
        else:
            a = m
    return (a + b) / 2.0

def newton_raphson(w0, tol=1e-5, max_iter=100):
    w_curr = w0
    for _ in range(max_iter):
        w_next = w_curr - f(w_curr) / df(w_curr)
        if abs(w_next - w_curr) < tol:
            return w_next
        w_curr = w_next
    raise ValueError("Newton-Raphson method did not converge.")

def secant(w0, w1, tol=1e-5, max_iter=100):
    for _ in range(max_iter):
        if abs(f(w1) - f(w0)) < 1e-12:
            raise ValueError("Function values at w0 and w1 are too close.")
        w_next = w1 - f(w1) * (w1 - w0) / (f(w1) - f(w0))
        if abs(w_next - w1) < tol:
            return w_next
        w0, w1 = w1, w_next
    raise ValueError("Secant method did not converge.")

# Example usage
g = 9.81  # gravitational acceleration
target_x = 1.0  # target value for the function
a, b = 0.1, 2.0  # interval for bise

# Bisection method
try:
    root_bisection = bisection(a, b)
    print(f"Bisection method root: {root_bisection}")
except ValueError as e:
    print(f"Bisection method error: {e}")

# Newton-Raphson method
try:
    root_newton = newton_raphson(1.0)
    print(f"Newton-Raphson method root: {root_newton}")
except ValueError as e:
    print(f"Newton-Raphson method error: {e}")

# Secant method
try:
    root_secant = secant(0.5, 1.5)
    print(f"Secant method root: {root_secant}")
except ValueError as e:
    print(f"Secant method error: {e}")
