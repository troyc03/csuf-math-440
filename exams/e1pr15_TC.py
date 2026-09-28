import numpy as np

def matrix_norm_inf(A):
    max_sum = 0.0
    for i in range(A.shape[0]):
        row_sum = np.sum(np.abs(A[i, :]))
        if row_sum > max_sum:
            max_sum = row_sum
    return max_sum

def matrix_norm_2(A):
    AtA = A.T @ A
    eigenvalues = np.linalg.eigvals(AtA)
    return np.sqrt(np.max(eigenvalues))

A_test = np.array([[1, 2], [3, 4]])
inf_norm = matrix_norm_inf(A_test)
two_norm = matrix_norm_2(A_test)
print(f"Infinity norm of A: {inf_norm}")
print(f"2-norm of A: {two_norm}")
