import numpy as np


def approximate_surface_potential(Vg, Vfb=0):
    """
    Approximate surface potential from gate voltage.

    Parameters
    ----------
    Vg : ndarray
        Gate voltage array

    Vfb : float
        Flat-band voltage

    Returns
    -------
    ndarray
        Surface potential
    """

    return np.maximum(Vg - Vfb, 0)