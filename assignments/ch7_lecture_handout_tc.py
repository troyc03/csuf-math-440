# Troy Chin

import numpy as np

print('=' * 50)
print('                   Exercise 1                ')
print('=' * 50)

def l1_norm(x):
    return np.sum(np.abs(x))

def l2_norm(x):
    return np.sum(np.sqrt(x)**2)

# Example usage
x1 = np.array([1,2,3])
x2 = np.array([2,4,6])

print('L1 (Manhattan) Norm: ', l1_norm(x1))
print('L2 (Euclidean) Norm: ', l2_norm(x2))

print('=' * 50)
print('                   Exercise 2                ')
print('=' * 50)

def l_inf_norm(x):
    return np.max(np.abs(x))

v1 = np.array([1,2,3])
print('Inf Norm: ', l_inf_norm(v1))

print('=' * 50)
print('                   Exercise 3                ')
print('=' * 50)

def l2_dist(x, y):
    return np.sum(np.sqrt((x - y)**2))

v1 = np.array([1, 2, 3])
v2 = np.array([2, 4, 6])

print('L2 (Euclidean) Distance: ', l2_dist(v1, v2))

print('=' * 50)
print('                   Exercise 4                ')
print('=' * 50)

def l_inf_dist(x, y):
    return np.max(np.abs((x - y)))

v1 = np.array([1, 2, 3])
v2 = np.array([2, 4, 6])

print('Infinity Distance: ', l_inf_dist(v1, v2))

