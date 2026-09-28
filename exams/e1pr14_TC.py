import numpy as np

def e1pr14_TC(x_vector, tol=1e-5):
    x_curr = np.array(x_vector, dtype=float)
    N = 0
    while True:
        N += 1
        x_next = x_curr / 2.0
        diff = np.max(np.abs(x_next - x_curr))
        if diff < tol:
            return N
        x_curr = x_next

x_test = [1, 2, 3, 4, 5]
iters = e1pr14_TC(x_test)
print(f"Number of iterations to converge: {iters}")
