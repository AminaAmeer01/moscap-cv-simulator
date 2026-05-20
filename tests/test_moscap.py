import math
import pytest

from src.physics.semiconductor import intrinsic_carrier_concentration

from src.physics.moscap import (
    oxide_capacitance,
    depletion_width,
    semiconductor_capacitance,
    total_capacitance,
)


def test_oxide_capacitance_positive():
    """Capacitance should be positive for valid inputs."""
    C = oxide_capacitance(area=1e-6, tox=1e-9)
    assert C > 0


def test_depletion_width_increases_with_phi():
    """Depletion width should increase with surface potential."""
    N_A = 1e23

    W1 = depletion_width(0.1, N_A)
    W2 = depletion_width(0.3, N_A)

    assert W2 > W1


def test_semiconductor_capacitance_decreases_with_phi():
    """Semiconductor capacitance should decrease as depletion increases."""
    N_A = 1e23
    area = 1e-6

    C1 = semiconductor_capacitance(0.1, N_A, area)
    C2 = semiconductor_capacitance(0.4, N_A, area)

    assert C2 < C1


def test_total_capacitance_series_behavior():
    """Total capacitance should be less than individual capacitances (series rule)."""
    C_ox = 1e-6
    C_s = 1e-7

    C_total = total_capacitance(C_ox, C_s)

    assert C_total < C_ox
    assert C_total < C_s


def test_no_nan_outputs():
    """Ensure functions do not return NaN values."""
    C = oxide_capacitance(1e-6)
    assert not math.isnan(C)

def test_intrinsic_carrier_positive():
    """
    Intrinsic carrier concentration must remain positive.
    """
    ni = intrinsic_carrier_concentration(300)

    assert ni > 0

def test_intrinsic_carrier_increases_with_temperature():

    """
    Intrinsic carrier concentration should increase with temperature.
    """
    ni_low = intrinsic_carrier_concentration(250)
    ni_high = intrinsic_carrier_concentration(350)

    assert ni_high > ni_low

def test_negative_temperature_raises():
    """
    Negative temperature should raise ValueError.
    """
    with pytest.raises(ValueError):
        intrinsic_carrier_concentration(-100)

def test_negative_area_raises():
    """
    Negative capacitor area should raise ValueError.
    """
    with pytest.raises(ValueError):
        oxide_capacitance(-1e-6)