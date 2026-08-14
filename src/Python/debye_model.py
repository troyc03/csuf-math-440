import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import fixed_quad

def cv(T):
    """
    Calculates the heat capacity C_V of a solid aluminum sample at temperature T.
    Uses SciPy's fixed-order Gaussian quadrature with N=50 sample points.
    """
    # 1. Define physical constants (SI units)
    V = 1000 * 1e-6          # Convert 1000 cubic centimeters to m^3
    rho = 6.022e28           # Number density in m^-3
    k_B = 1.380649e-23       # Boltzmann constant in J/K
    theta_D = 428.0          # Debye temperature of aluminum in K
    
    # 2. Handle zero or near-zero temperature boundary conditions
    if T < 1e-5:
        return 0.0
    
    # 3. Define the integrand with numerical safeguards
    def integrand(x):
        # Prevent runtime overflow/underflow errors inside the exponential
        with np.errstate(over='ignore', under='ignore'):
            exp_x = np.exp(x)
            # Avoid division by zero if x is exceptionally close to 0
            denominator = (exp_x - 1) ** 2
            denominator = np.where(denominator == 0, 1e-20, denominator)
            return (x**4 * exp_x) / denominator

    # 4. Set integration limits
    a = 0.0
    b = theta_D / T
    
    # 5. Compute the integral using Gaussian quadrature with exactly N=50 points
    integral, _ = fixed_quad(integrand, a, b, n=50)
    
    # 6. Apply the prefactor to get final C_V
    prefactor = 9 * V * rho * k_B * (T / theta_D)**3
    return prefactor * integral

if __name__ == "__main__":
    # Generate an array of 500 temperature steps from 5 K to 500 K
    temperatures = np.linspace(5, 500, 500)
    
    # Calculate C_V values using a list comprehension
    cv_values = [cv(T) for T in temperatures]
    
    # Configure and display the plot
    plt.figure(figsize=(9, 5.5))
    plt.plot(temperatures, cv_values, label=r'Debye Model $C_V(T)$', color='darkblue', linewidth=2)
    
    # Formatting elements
    plt.title('Heat Capacity of Solid Aluminum ($1000 cm^3$)', fontsize=14, pad=15)
    plt.xlabel('Temperature $T$ (K)', fontsize=12)
    plt.ylabel('Heat Capacity $C_V$ (J/K)', fontsize=12)
    plt.grid(True, linestyle='--', alpha=0.5)
    plt.xlim(0, 500)
    plt.ylim(bottom=0)
    plt.legend(fontsize=11, loc='lower right')
    
    # Display the final visualization window
    plt.tight_layout()
    plt.show()
