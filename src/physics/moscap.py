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
