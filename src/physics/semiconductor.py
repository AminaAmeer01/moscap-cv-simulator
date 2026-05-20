"""
Semiconductor physics functions.
"""

import numpy as np
from .constants import k_B, q, ni_300K, Eg_300K


def intrinsic_carrier_concentration(T: float) -> float:
    """
    Compute intrinsic carrier concentration as a function of temperature.

    Parameters
    ----------
    T : float
        Temperature in Kelvin

    Returns
    -------
    float
        Intrinsic carrier concentration (1/m^3)
    """
    if T <= 0:
        raise ValueError("Temperature must be positive")

    T0 = 300  # reference temperature (K)

    # Convert bandgap from eV to Joules
    Eg_J = Eg_300K * q

    ni = ni_300K * (T / T0) ** (3/2) * np.exp(
        -Eg_J / (2 * k_B) * (1 / T - 1 / T0)
    )

    return ni

