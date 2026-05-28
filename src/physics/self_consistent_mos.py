import numpy as np

from .constants import q, epsilon_si, k_B

def charge_density(phi, N_A, ni, T=300):
    """
    Semiconductor charge density using Boltzmann statistics.

    Parameters
    ----------
    phi : ndarray
        Electrostatic potential

    N_A : float
        Acceptor doping concentration

    ni : float
        Intrinsic carrier concentration

    T : float
        Temperature in Kelvin
    """

    Vt = k_B * T / q

    # Electron concentration
    n = ni * np.exp(phi / Vt)

    # Hole concentration
    p = ni * np.exp(-phi / Vt)

    # Charge density
    rho = q * (p - n - N_A)

    return rho


def solve_potential(phi_init, dx, N_A, ni, iterations=500):
    """
    Self-consistent Poisson solver.
    """

    phi = phi_init.copy()

    N = len(phi)

    for _ in range(iterations):

        phi_old = phi.copy()

        rho = charge_density(phi, N_A, ni)

        for i in range(1, N - 1):
            phi[i] = 0.5 * (
                    phi[i + 1]
                    + phi[i - 1]
                    + dx ** 2 * rho[i] / epsilon_si
            )

        error = np.max(np.abs(phi - phi_old))

        if error < 1e-8:
            break

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

        Qs = np.sum(charge_density(phi, N_A, ni)) * dx

        C = np.abs(Qs / max(V, 1e-9))

        results.append(C)

    return np.array(Vg), np.array(results)