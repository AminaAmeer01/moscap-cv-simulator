import numpy as np
import matplotlib.pyplot as plt

from .electrostatics import approximate_surface_potential
from .semiconductor import intrinsic_carrier_concentration
from .moscap import (
    oxide_capacitance,
    semiconductor_capacitance,
    total_capacitance,
    mos_capacitance_regime,
)


def compute_intrinsic_vs_temperature(temperatures):
    """
    Compute intrinsic carrier concentration as a function of temperature.

    Parameters
    ----------
    temperatures : ndarray
        Temperature values in Kelvin.

    Returns
    -------
    tuple
        Temperature array and intrinsic carrier concentration array.
    """

    ni_values = []

    for T in temperatures:
        ni_values.append(
            intrinsic_carrier_concentration(T)
        )

    return np.array(temperatures), np.array(ni_values)


def plot_intrinsic_vs_temperature(T, ni):
    """
    Plot intrinsic carrier concentration versus temperature.
    """

    plt.figure()

    plt.plot(T, ni)

    plt.xlabel("Temperature (K)")
    plt.ylabel("Intrinsic Carrier Concentration (1/m³)")
    plt.title("Intrinsic Carrier Concentration vs Temperature")

    plt.grid()

    return plt


def compute_cv_curve(Vg, N_A, area):
    """
    Compute MOS capacitance-voltage curve from gate voltage.

    Parameters
    ----------
    Vg : ndarray
        Gate voltage values.

    N_A : float
        Acceptor concentration.

    area : float
        Capacitor area.

    Returns
    -------
    tuple
        Gate voltage array and capacitance array.
    """

    C_ox = oxide_capacitance(area)

    phi_s = approximate_surface_potential(Vg)

    C_total = []

    for phi in phi_s:

        C_s = semiconductor_capacitance(
            phi + 1e-9,
            N_A,
            area
        )

        C = total_capacitance(
            C_ox,
            C_s
        )

        C_total.append(C)

    return np.array(Vg), np.array(C_total)


def compute_cv_curve_advanced(phi_s, N_A, area):
    """
    Compute regime-aware MOS capacitance.

    Parameters
    ----------
    phi_s : ndarray
        Surface potential values.

    N_A : float
        Acceptor concentration.

    area : float
        Capacitor area.

    Returns
    -------
    tuple
        Surface potential array and capacitance array.
    """

    C_ox = oxide_capacitance(area)

    C_total = []

    for phi in phi_s:

        C = mos_capacitance_regime(
            phi,
            N_A,
            area,
            C_ox
        )

        C_total.append(C)

    return np.array(phi_s), np.array(C_total)

def compute_theoretical_cv(
        phi_s,
        N_A,
        area
):
    """
    Compute analytical MOS capacitance curve.

    Parameters
    ----------
    phi_s : ndarray
        Surface potential values.

    N_A : float
        Acceptor concentration.

    area : float
        Capacitor area.

    Returns
    -------
    ndarray
        Analytical MOS capacitance.
    """

    C_ox = oxide_capacitance(area)

    C_theory = []

    for phi in phi_s:

        C_s = semiconductor_capacitance(
            phi,
            N_A,
            area
        )

        C_total = total_capacitance(
            C_ox,
            C_s
        )

        C_theory.append(C_total)

    return np.array(C_theory)

def plot_cv_curve(phi_s, C_total):
    """
    Plot MOS capacitance-voltage curve.
    """

    plt.figure()

    plt.plot(phi_s, C_total)

    plt.xlabel("Surface Potential (V)")
    plt.ylabel("Capacitance (F)")
    plt.title("MOS Capacitor C–V Characteristics")

    plt.grid()

    return plt


def compute_cv_vs_temperature(
        phi_s,
        temperatures,
        N_A,
        area
):
    """
    Compute MOS capacitance curves for multiple temperatures.
    """

    results = {}

    for T in temperatures:
        ni = intrinsic_carrier_concentration(T)

        phi, C = compute_cv_curve_advanced(
            phi_s,
            N_A,
            area
        )

        scale = (
                ni /
                intrinsic_carrier_concentration(300)
        )

        results[T] = C * scale

    return phi, results


def plot_cv_vs_temperature(phi_s, results):
    """
    Plot temperature-dependent MOS capacitance.
    """

    plt.figure()

    for T, C in results.items():

        plt.plot(
            phi_s,
            C,
            label=f"T = {T} K"
        )

    plt.xlabel("Gate Voltage (V)")
    plt.ylabel("Capacitance (F)")
    plt.title("Temperature-Dependent MOS C–V")

    plt.legend()
    plt.grid()

    return plt


def compute_doping_sweep(
        phi_s,
        doping_values,
        area
):
    """
    Compute MOS capacitance curves for multiple doping levels.
    """

    results = {}

    for N_A in doping_values:

        _, C = compute_cv_curve_advanced(
            phi_s,
            N_A,
            area
        )

        results[N_A] = C

    return phi_s, results


def compute_tox_sweep(
        phi_s,
        tox_values,
        area,
        N_A=1e23
):
    """
    Compute MOS capacitance curves for multiple oxide thicknesses.
    """

    results = {}

    for tox in tox_values:

        C_ox = oxide_capacitance(
            area,
            tox
        )

        C_total = []

        for phi in phi_s:

            C = mos_capacitance_regime(
                phi,
                N_A,
                area,
                C_ox
            )

            C_total.append(C)

        results[tox] = np.array(C_total)

    return phi_s, results


def compute_gate_voltage_sweep(
        Vg,
        N_A,
        area
):
    """
    Compute advanced MOS C-V as a function of gate voltage.
    """

    phi_s = approximate_surface_potential(Vg)

    _, C = compute_cv_curve_advanced(
        phi_s,
        N_A,
        area
    )

    return np.array(Vg), np.array(C)

def compute_error_analysis(
        phi_s,
        N_A,
        area
):
    """
    Compare analytical and numerical MOS C-V
    and compute error metrics.
    """

    C_theory = compute_theoretical_cv(
        phi_s,
        N_A,
        area
    )

    _, C_num = compute_cv_curve_advanced(
        phi_s,
        N_A,
        area
    )

    relative_error = np.abs(
        (C_num - C_theory) / C_theory
    )

    mean_error = np.mean(
        relative_error
    )

    max_error = np.max(
        relative_error
    )

    rms_error = np.sqrt(
        np.mean(relative_error ** 2)
    )

    return (
        phi_s,
        relative_error,
        mean_error,
        max_error,
        rms_error
    )

def compute_theory_comparison(
        phi_s,
        N_A,
        area
):
    """
    Compare analytical and regime-aware MOS models.
    """

    C_theory = compute_theoretical_cv(
        phi_s,
        N_A,
        area
    )

    _, C_num = compute_cv_curve_advanced(
        phi_s,
        N_A,
        area
    )

    return (
        phi_s,
        C_theory,
        C_num
    )
