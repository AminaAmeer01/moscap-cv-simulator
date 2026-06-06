import numpy as np

from .simulation import compute_cv_curve_advanced


def doping_sweep(
    doping_values,
    Vg
):
    """
    Compute C-V curves for multiple doping concentrations.
    """

    results = {}

    for N_A in doping_values:

        V, C = compute_cv_curve_advanced(
            Vg,
            N_A=N_A
        )

        results[N_A] = (V, C)

    return results

def oxide_sweep(
    oxide_thicknesses,
    Vg
):
    """
    Compute C-V curves for multiple oxide thicknesses.
    """

    results = {}

    for tox in oxide_thicknesses:

        V, C = compute_cv_curve_advanced(
            Vg,
            tox=tox
        )

        results[tox] = (V, C)

    return results