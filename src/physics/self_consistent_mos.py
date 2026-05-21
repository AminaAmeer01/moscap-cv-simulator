import numpy as np

from .constants import q, epsilon_si


def charge_density(phi, N_A, ni):
    """
    Simplified charge density model.
    """

    p = N_A * np.exp(-phi)
    n = ni * np.exp(phi)

    return q * (p - n - N_A)


def solve_potential(phi_init, dx, N_A, ni, iterations=500):
    """
    Self-consistent Poisson solver.
    """

    phi = phi_init.copy()

    N = len(phi)

    for _ in range(iterations):

        rho = charge_density(phi, N_A, ni)

        for i in range(1, N - 1):
            phi[i] = 0.5 * (
                phi[i+1]
                + phi[i-1]
                + dx**2 * rho[i] / epsilon_si
            )

    return phi


def surface_potential(phi):
    """
    Extract surface potential.
    """

    return phi[-1]


def compute_self_consistent_cv(Vg, N_A, ni, dx=1e-9):
    """
    Compute self-consistent MOS C-V.
    """

    results = []

    for V in Vg:

        phi_init = np.zeros(50)

        phi = solve_potential(phi_init, dx, N_A, ni)

        phi_s = surface_potential(phi)

        C = epsilon_si / dx

        results.append(C)

    return np.array(Vg), np.array(results)