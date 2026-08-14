import numpy as np
import pandas as pd


def f(x):
    """The function to differentiate: f(x) = x(x - 1)"""
    return x * (x - 1)


def calculate_derivatives(x, deltas):
    """Calculates forward, backward, and central finite differences."""
    results = []
    true_derivative = 1.0  # Analytical result at x = 1

    for delta in deltas:
        # 1. Forward Difference
        f_forward = (f(x + delta) - f(x)) / delta
        err_forward = abs(f_forward - true_derivative)

        # 2. Backward Difference
        f_backward = (f(x) - f(x - delta)) / delta
        err_backward = abs(f_backward - true_derivative)

        # 3. Central Difference
        f_central = (f(x + delta) - f(x - delta)) / (2 * delta)
        err_central = abs(f_central - true_derivative)

        results.append(
            {
                "Delta": f"10^{int(np.log10(delta))}",
                "Forward Ans": f_forward,
                "Forward Err": err_forward,
                "Backward Ans": f_backward,
                "Backward Err": err_backward,
                "Central Ans": f_central,
                "Central Err": err_central,
            }
        )

    return pd.DataFrame(results)


# Configuration
target_x = 1.0
test_deltas = [1e-2, 1e-4, 1e-6, 1e-8, 1e-10, 1e-12, 1e-14]

# Run calculation
df_results = calculate_derivatives(target_x, test_deltas)

# Display formatted results
print('\n')
pd.set_option("display.max_columns", None)
pd.set_option("display.width", 1000)
pd.set_option("display.float_format", lambda x: f"{x:.16f}")
print(df_results.to_string(index=False))
print('\n')
