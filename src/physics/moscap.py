from .constants import epsilon_0, epsilon_ox, tox_default

def oxide_capacitance(area: float, tox: float = tox_default) -> float:
    """
    Calculate the oxide capacitance per unit area of a MOS capacitor.

    Parameters
    ----------
    area : float
        Area of the capacitor in m^2
    tox : float
        Oxide thickness in meters (default: 5e-9 m)

    Returns
    -------
    float
        Capacitance in Farads
    """
    return epsilon_ox * area / tox


from .constants import epsilon_si, q


def depletion_width(phi_s: float, N_A: float) -> float:
    """
    Compute depletion width in a p-type semiconductor.

    Parameters
    ----------
    phi_s : float
        Surface potential (V)
    N_A : float
        Acceptor doping concentration (1/m^3)

    Returns
    -------
    float
        Depletion width (m)
    """
    return (2 * epsilon_si * phi_s / (q * N_A)) ** 0.5
