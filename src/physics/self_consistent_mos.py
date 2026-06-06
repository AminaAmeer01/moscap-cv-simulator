import numpy as np

from .constants import q, epsilon_si, k_B


# ============================================================
# 1. CHARGE DENSITY (Boltzmann statistics)
# ============================================================

def charge_density(phi, N_A, ni, T=300):
    """
    Compute semiconductor charge density using Boltzmann statistics.

    Parameters
    ----------
    phi : ndarray
        Electrostatic potential.

    N_A : float
        Acceptor concentration.

    ni : float
        Intrinsic carrier concentration.

    T : float
        Temperature (K).

    Returns
    -------
    ndarray
        Charge density profile.
    """

    Vt = k_B * T / q

    # Prevent overflow in exp()
    phi_limited = np.clip(phi, -0.5, 0.5)

    n = ni * np.exp(phi_limited / Vt)
    p = ni * np.exp(-phi_limited / Vt)

    rho = q * (p - n - N_A)

    return rho


# ============================================================
# 2. POISSON SOLVER (Finite difference, Jacobi iteration)
# ============================================================

def solve_potential(
    phi_init,
    dx,
    N_A,
    ni,
    gate_voltage=0.0,
    iterations=500,
    tol=1e-8
):
    """
    Self-consistent 1D Poisson solver using finite differences.

    Parameters
    ----------
    phi_init : ndarray
        Initial potential guess.

    dx : float
        Spatial grid spacing.

    N_A : float
        Acceptor concentration.

    ni : float
        Intrinsic carrier concentration.

    gate_voltage : float
        Applied gate voltage.

    iterations : int
        Maximum iterations.

    tol : float
        Convergence tolerance.

    Returns
    -------
    ndarray
        Converged potential profile.
    """

    phi = phi_init.copy()
    N = len(phi)

    phi[0] = 0.0
    phi[-1] = gate_voltage

    for _ in range(iterations):

        phi_old = phi.copy()

        rho = charge_density(phi, N_A, ni)

        for i in range(1, N - 1):

            new_phi = 0.5 * (
                phi[i + 1]
                + phi[i - 1]
                + dx**2 * rho[i] / epsilon_si
            )

            # Numerical stabilization
            phi[i] = np.clip(new_phi, -1.0, 1.0)

        phi[0] = 0.0
        phi[-1] = gate_voltage

        error = np.max(np.abs(phi - phi_old))

        if error < tol:
            break

    return phi


# ============================================================
# 3. OBSERVABLES
# ============================================================

def surface_potential(phi):
    """
    Return surface potential.
    """
    return phi[-1]


def electric_field(phi, dx):
    """
    Compute electric field from potential profile.
    """
    return -np.gradient(phi, dx)


def total_charge_density(rho, dx):
    """
    Compute total semiconductor charge.
    """
    return np.trapezoid(rho, dx=dx)


# ============================================================
# 4. MOS REGIME CLASSIFICATION
# ============================================================

def mos_regime(phi_s, phi_f):
    """
    Classify MOS operating regime.
    """

    if phi_s < 0:
        return "accumulation"
    elif phi_s < 2 * phi_f:
        return "depletion"
    else:
        return "inversion"


# ============================================================
# 5. SELF-CONSISTENT C–V
# ============================================================

def compute_self_consistent_cv(
    Vg,
    N_A,
    ni,
    dx=1e-9,
    N=50
):
    """
    Compute self-consistent MOS C–V curve.

    Parameters
    ----------
    Vg : ndarray
        Gate-voltage sweep.

    N_A : float
        Acceptor concentration.

    ni : float
        Intrinsic carrier concentration.

    dx : float
        Spatial grid spacing.

    N : int
        Number of grid points.

    Returns
    -------
    tuple
        (Gate voltage, capacitance)
    """

    Q_list = []
    phi_list = []
    regime_list = []

    for V in Vg:

        phi_init = np.zeros(N)

        phi = solve_potential(
            phi_init,
            dx,
            N_A,
            ni,
            gate_voltage=V
        )

        rho = charge_density(phi, N_A, ni)

        Qs = total_charge_density(rho, dx)

        phi_s = surface_potential(phi)

        Q_list.append(Qs)
        phi_list.append(phi_s)

        phi_f = 0.3

        regime_list.append(
            mos_regime(phi_s, phi_f)
        )

    Q_list = np.array(Q_list)

    # Physics-based capacitance definition
    C = np.abs(np.gradient(Q_list, Vg))

    # Remove NaN/Inf values
    C = np.nan_to_num(
        C,
        nan=0.0,
        posinf=0.0,
        neginf=0.0
    )

    return np.array(Vg), C