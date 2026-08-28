import numpy as np
from numpy.linalg import *

print('\n======= PROBLEM 2A =======\n')

A = np.array([
    [2, -3, 6],
    [0, 3, -4],
    [0, 2, -3]
])

eigenvalues, eigenvectors = eig(A)
print(f'Eigenvalues: {eigenvalues}\n')
print(f'Eigenvectors: {eigenvectors}\n')

if eigenvalues[0] != eigenvalues[1] != eigenvalues[2]:
    print(f'All eigenvalues are distinct.\n')

# If rank equals 3, the columns are linearly independent.
is_independent = matrix_rank(eigenvectors)
print(f'Rank: {is_independent}\n')

if is_independent:
    print("Yes, there is a set of three linearly independent eigenvectors.")
else:
    print("No, the eigenvectors are linearly dependent.")

print('\n======= PROBLEM 2A =======\n')

A = np.array([
    [1, 0, 0],
    [-1, 0, 1],
    [-1, -1, 2]
])

eigenvalues, eigenvectors = eig(A)
print(f'Eigenvalues: {eigenvalues}\n')
print(f'Eigenvectors: {eigenvectors}\n')

if eigenvalues[0] != eigenvalues[1] != eigenvalues[2]:
    print(f'All eigenvalues are distinct.\n')

# If rank equals 3, the columns are linearly independent.
is_independent = matrix_rank(eigenvectors)
print(f'Rank: {is_independent}\n')

if is_independent:
    print("Yes, there is a set of three linearly independent eigenvectors.")
else:
    print("No, the eigenvectors are linearly dependent.")

