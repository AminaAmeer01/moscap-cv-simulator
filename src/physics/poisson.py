import numpy as np

def solve_poisson_1d(rho, dx, epsilon, iterations=1000):
    """
    Simple 1D finite-difference Poisson solver.

    Parameters
    ----------
    rho : ndarray
        Charge density
    dx : float
        Spatial step
    epsilon : float
        Permittivity
    """

    N = len(rho)

    phi = np.zeros(N)

    for _ in range(iterations):
        for i in range(1, N - 1):
            phi[i] = 0.5 * (
                phi[i+1]
                + phi[i-1]
                + dx**2 * rho[i] / epsilon
            )

    return phi