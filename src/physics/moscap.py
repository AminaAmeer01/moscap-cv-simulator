from .constants import epsilon_ox, tox_default, epsilon_si, q


def oxide_capacitance(area: float, tox: float = tox_default) -> float:
    return epsilon_ox * area / tox


def depletion_width(phi_s: float, N_A: float) -> float:
    return (2 * epsilon_si * phi_s / (q * N_A)) ** 0.5


def semiconductor_capacitance(phi_s: float, N_A: float, area: float) -> float:
    # Avoid division by zero
    phi_s_safe = max(phi_s, 1e-9)
    W = depletion_width(phi_s_safe, N_A)
    return epsilon_si * area / W


def total_capacitance(C_ox: float, C_s: float) -> float:
    return 1 / (1 / C_ox + 1 / C_s)


def flat_band_voltage(phi_ms: float, Q_ox: float, C_ox: float) -> float:
    return phi_ms - Q_ox / C_ox


def mos_capacitance_regime(phi_s: float, N_A: float, area: float, C_ox: float) -> float:
    """
    Simplified MOS capacitance model:
    - Accumulation → C ≈ Cox
    - Depletion → series combination
    - Strong inversion → C ≈ Cox (low-frequency approximation)
    """

    # Accumulation
    if phi_s < 0:
        return C_ox

    # Approximate transition (≈ 2*phi_F)
    elif phi_s < 0.4:
        C_s = semiconductor_capacitance(phi_s, N_A, area)
        return total_capacitance(C_ox, C_s)

    # Strong inversion
    else:
        return C_ox