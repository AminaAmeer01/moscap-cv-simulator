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
    Compute intrinsic carrier concentration vs temperature.
    """
    ni_values = []

    for T in temperatures:
        ni = intrinsic_carrier_concentration(T)
        ni_values.append(ni)

    return np.array(temperatures), np.array(ni_values)


def plot_intrinsic_vs_temperature(T, ni):
    """
    Plot intrinsic carrier concentration vs temperature.
    """
    plt.figure()
    plt.plot(T, ni)
    plt.xlabel("Temperature (K)")
    plt.ylabel("Intrinsic Carrier Concentration (1/m^3)")
    plt.title("Intrinsic Carrier Concentration vs Temperature")
    plt.grid()
    return plt


def compute_cv_curve(Vg, N_A, area):
    """
    Compute MOS C-V curve from gate voltage.
    """

    C_ox = oxide_capacitance(area)

    # Compute surface potential from gate voltage
    phi_s = approximate_surface_potential(Vg)

    C_total = []

    for phi in phi_s:
        C_s = semiconductor_capacitance(phi + 1e-9, N_A, area)

        C = total_capacitance(C_ox, C_s)

        C_total.append(C)

    return np.array(Vg), np.array(C_total)

def compute_cv_curve_advanced(phi_s, N_A, area):
    """
    Advanced MOS C-V including regimes.
    """
    C_ox = oxide_capacitance(area)

    C_total = []

    for phi in phi_s:
        C = mos_capacitance_regime(phi, N_A, area, C_ox)
        C_total.append(C)

    return np.array(phi_s), np.array(C_total)

def plot_cv_curve(phi_s, C_total):
    """
    Plot MOS C-V curve.
    """
    plt.figure()
    plt.plot(phi_s, C_total)
    plt.xlabel("Surface Potential (V)")
    plt.ylabel("Capacitance (F)")
    plt.title("MOS Capacitor C–V Characteristics")
    plt.grid()
    return plt

def compute_cv_vs_temperature(phi_s, temperatures, N_A, area):
    """
    Compute MOS C-V curves for multiple temperatures.

    Returns
    -------
    dict:
        {T: capacitance array}
    """
    results = {}

    for T in temperatures:
        ni = intrinsic_carrier_concentration(T)

        phi, C = compute_cv_curve(phi_s, N_A, area)

        # Apply temperature scaling (simple physical model)
        scale = ni / intrinsic_carrier_concentration(300)
        C_T = C * scale

        results[T] = C_T

    return phi, results

def plot_cv_vs_temperature(phi_s, results):
    """
    Plot C-V curves for multiple temperatures.
    """
    plt.figure()

    for T, C in results.items():
        plt.plot(phi_s, C, label=f"T = {T} K")

    plt.xlabel("Gate Voltage (V)")
    plt.ylabel("Capacitance (F)")
    plt.title("Temperature-Dependent MOS C–V")
    plt.legend()
    plt.grid()

    return plt