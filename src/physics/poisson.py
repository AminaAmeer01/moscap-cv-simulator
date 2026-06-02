import numpy as np

def solve_poisson_1d(
        rho,
        dx,
        epsilon,
        left_bc=0.0,
        right_bc=0.0,
        iterations=1000
):
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

left_bc : float
    Left boundary potential

right_bc : float
    Right boundary potential

Returns
-------
ndarray
    Electrostatic potential profile
"""
    N = len(rho)

    phi = np.zeros(N)

    phi[0] = left_bc
    phi[-1] = right_bc

    for _ in range(iterations):
        for i in range(1, N - 1):
            phi[i] = 0.5 * (
                phi[i+1]
                + phi[i-1]
                + dx**2 * rho[i] / epsilon
            )

    return phi