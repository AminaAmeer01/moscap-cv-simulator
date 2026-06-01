"""
MOS capacitor physics functions.
"""

from .constants import (
    epsilon_ox,
    epsilon_si,
    q,
    tox_default,
)

from .electrostatics import strong_inversion_voltage


def oxide_capacitance(
    area: float,
    tox: float = tox_default
) -> float:
    """
    Calculate oxide capacitance.

    Parameters
    ----------
    area : float
        Capacitor area (m²).

    tox : float
        Oxide thickness (m).

    Returns
    -------
    float
        Oxide capacitance (F).
    """

    if area <= 0:
        raise ValueError(
            "Capacitor area must be positive."
        )

    if tox <= 0:
        raise ValueError(
            "Oxide thickness must be positive."
        )

    return epsilon_ox * area / tox


def depletion_width(
    phi_s: float,
    N_A: float
) -> float:
    """
    Compute semiconductor depletion width.

    Parameters
    ----------
    phi_s : float
        Surface potential (V).

    N_A : float
        Acceptor concentration (1/m³).

    Returns
    -------
    float
        Depletion width (m).
    """

    if N_A <= 0:
        raise ValueError(
            "Doping concentration must be positive."
        )

    if phi_s < 0:
        raise ValueError(
            "Surface potential must be non-negative."
        )

    return (2 * epsilon_si * phi_s / (q * N_A)) ** 0.5


def semiconductor_capacitance(
    phi_s: float,
    N_A: float,
    area: float
) -> float:
    """
    Compute semiconductor depletion capacitance.

    Parameters
    ----------
    phi_s : float
        Surface potential (V).

    N_A : float
        Acceptor concentration (1/m³).

    area : float
        Capacitor area (m²).

    Returns
    -------
    float
        Semiconductor capacitance (F).
    """

    if area <= 0:
        raise ValueError(
            "Capacitor area must be positive."
        )

    W = depletion_width(phi_s, N_A)

    return epsilon_si * area / W


def total_capacitance(
    C_ox: float,
    C_s: float
) -> float:
    """
    Compute total MOS capacitance using series combination.

    Parameters
    ----------
    C_ox : float
        Oxide capacitance (F).

    C_s : float
        Semiconductor capacitance (F).

    Returns
    -------
    float
        Total capacitance (F).
    """

    if C_ox <= 0:
        raise ValueError(
            "Oxide capacitance must be positive."
        )

    if C_s <= 0:
        raise ValueError(
            "Semiconductor capacitance must be positive."
        )

    return 1.0 / (1.0 / C_ox + 1.0 / C_s)


def flat_band_voltage(
    phi_ms: float,
    Q_ox: float,
    C_ox: float
) -> float:
    """
    Compute flat-band voltage.

    Parameters
    ----------
    phi_ms : float
        Metal-semiconductor work function difference.

    Q_ox : float
        Oxide charge density.

    C_ox : float
        Oxide capacitance.

    Returns
    -------
    float
        Flat-band voltage (V).
    """

    if C_ox <= 0:
        raise ValueError(
            "Oxide capacitance must be positive."
        )

    return phi_ms - Q_ox / C_ox


def mos_capacitance_regime(
    phi_s: float,
    N_A: float,
    area: float,
    C_ox: float,
    n_i: float = 1.0e16,
    T: float = 300.0,
) -> float:
    """
    Regime-aware MOS capacitance model.

    Regions
    -------
    Accumulation:
        C ≈ C_ox

    Depletion:
        C = (C_ox * C_s)/(C_ox + C_s)

    Strong Inversion:
        C ≈ C_ox (low-frequency approximation)

    Parameters
    ----------
    phi_s : float
        Surface potential (V).

    N_A : float
        Acceptor concentration (1/m³).

    area : float
        Device area (m²).

    C_ox : float
        Oxide capacitance (F).

    n_i : float
        Intrinsic carrier concentration (1/m³).

    T : float
        Temperature (K).

    Returns
    -------
    float
        MOS capacitance (F).
    """

    phi_inv = strong_inversion_voltage(
        N_A,
        n_i,
        T
    )

    # Accumulation
    if phi_s < 0:
        return C_ox

    # Depletion
    elif phi_s < phi_inv:

        C_s = semiconductor_capacitance(
            phi_s,
            N_A,
            area
        )

        return total_capacitance(
            C_ox,
            C_s
        )

    # Strong inversion
    else:
        return C_ox