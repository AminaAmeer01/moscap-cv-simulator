"""
Electrostatic relations for MOS capacitors.

This module contains simplified electrostatic models used
for MOS capacitor simulations.
"""

import numpy as np


def approximate_surface_potential(
    Vg: np.ndarray,
    Vfb: float = 0.0
) -> np.ndarray:
    """
    Approximate surface potential from gate voltage.

    This simplified model assumes that the surface potential
    follows the applied gate voltage after the flat-band
    voltage is exceeded.

    Parameters
    ----------
    Vg : np.ndarray
        Gate voltage array (V).

    Vfb : float, optional
        Flat-band voltage (V).

    Returns
    -------
    np.ndarray
        Surface potential array (V).
    """

    return np.maximum(Vg - Vfb, 0.0)


def fermi_potential(
    N_A: float,
    n_i: float,
    T: float = 300.0
) -> float:
    """
    Compute the Fermi potential of p-type silicon.

    Parameters
    ----------
    N_A : float
        Acceptor concentration (1/m^3).

    n_i : float
        Intrinsic carrier concentration (1/m^3).

    T : float, optional
        Temperature in Kelvin.

    Returns
    -------
    float
        Fermi potential (V).
    """

    k_B = 1.380649e-23
    q = 1.602176634e-19

    return (k_B * T / q) * np.log(N_A / n_i)


def strong_inversion_voltage(
    N_A: float,
    n_i: float,
    T: float = 300.0
) -> float:
    """
    Compute the strong inversion condition.

    Strong inversion occurs approximately when:

        phi_s = 2 * phi_F

    Parameters
    ----------
    N_A : float
        Acceptor concentration (1/m^3).

    n_i : float
        Intrinsic carrier concentration (1/m^3).

    T : float, optional
        Temperature (K).

    Returns
    -------
    float
        Strong inversion surface potential (V).
    """

    phi_F = fermi_potential(N_A, n_i, T)

    return 2.0 * phi_F