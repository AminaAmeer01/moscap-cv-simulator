import numpy as np

from src.physics.electrostatics import (
    fermi_potential,
    strong_inversion_voltage,
)

from src.physics.poisson import solve_poisson_1d

from src.physics.self_consistent_mos import (
    charge_density,
    solve_potential,
    compute_self_consistent_cv,
)

from src.physics.frequency import (
    high_frequency_capacitance,
    low_frequency_capacitance,
)

from src.physics.moscap import (
    flat_band_voltage,
    mos_capacitance_regime,
    oxide_capacitance,
)

from src.physics.self_consistent_mos import (
    surface_potential,
)

from src.physics.simulation import (
    compute_cv_curve_advanced,
)

def test_fermi_potential_positive():
    """
    Fermi potential should be positive for p-type silicon.
    """

    phi_f = fermi_potential(
        N_A=1e23,
        n_i=1e16
    )

    assert phi_f > 0


def test_strong_inversion_voltage_positive():
    """
    Strong inversion voltage should be positive.
    """

    phi_inv = strong_inversion_voltage(
        N_A=1e23,
        n_i=1e16
    )

    assert phi_inv > 0


def test_poisson_solver_shape():
    """
    Poisson solver output size must match input size.
    """

    rho = np.ones(100)

    phi = solve_poisson_1d(
        rho,
        dx=1e-9,
        epsilon=1e-10
    )

    assert len(phi) == len(rho)


def test_charge_density_shape():
    """
    Charge density output should match potential array size.
    """

    phi = np.zeros(50)

    rho = charge_density(
        phi,
        N_A=1e23,
        ni=1e16
    )

    assert len(rho) == len(phi)


def test_self_consistent_solver_shape():
    """
    Self-consistent potential solver should preserve grid size.
    """

    phi0 = np.zeros(50)

    phi = solve_potential(
        phi0,
        dx=1e-9,
        N_A=1e23,
        ni=1e16
    )

    assert len(phi) == len(phi0)


def test_self_consistent_cv_shape():
    """
    Self-consistent C-V solver should return matching arrays.
    """

    Vg = np.linspace(0.1, 1.0, 20)

    V, C = compute_self_consistent_cv(
        Vg,
        N_A=1e23,
        ni=1e16
    )

    assert len(V) == len(C)


def test_self_consistent_cv_positive():
    """
    Computed capacitances should be positive.
    """

    Vg = np.linspace(0.1, 1.0, 20)

    _, C = compute_self_consistent_cv(
        Vg,
        N_A=1e23,
        ni=1e16
    )

    assert np.all(C >= 0)

def test_self_consistent_convergence():
    """
    Self-consistent solver should converge
    to finite potential values.
    """

    phi0 = np.zeros(50)

    phi = solve_potential(
        phi0,
        dx=1e-9,
        N_A=1e23,
        ni=1e16
    )

    assert np.all(np.isfinite(phi))

def test_charge_density_finite():
    """
    Charge density calculation should remain finite.
    """

    phi = np.zeros(50)

    rho = charge_density(
        phi,
        N_A=1e23,
        ni=1e16
    )

    assert np.all(np.isfinite(rho))
def test_poisson_solver_finite():
    """
    Poisson solver should return finite values.
    """

    rho = np.ones(100)

    phi = solve_poisson_1d(
        rho,
        dx=1e-9,
        epsilon=1e-10
    )

    assert np.all(np.isfinite(phi))

def test_flat_band_voltage():
    """
    Flat-band voltage should equal work-function
    difference when oxide charge is zero.
    """

    Vfb = flat_band_voltage(
        phi_ms=0.2,
        Q_ox=0.0,
        C_ox=1e-6
    )

    assert Vfb == 0.2

def test_accumulation_regime():
    """
    Accumulation should return oxide capacitance.
    """

    C_ox = oxide_capacitance(1e-6)

    C = mos_capacitance_regime(
        -0.1,
        1e23,
        1e-6,
        C_ox
    )

    assert C == C_ox

def test_surface_potential():
    """
    Surface potential should be last node.
    """

    phi = np.array([0, 1, 2, 3])

    assert surface_potential(phi) == 3

def test_frequency_capacitances_positive():

    Cox = 1e-6
    Cs = 1e-7

    Chf = high_frequency_capacitance(Cox, Cs)
    Clf = low_frequency_capacitance(Cox)

    assert Chf > 0
    assert Clf > 0

def test_advanced_cv_curve():

    phi_s = np.linspace(-0.2, 1.0, 50)

    phi, C = compute_cv_curve_advanced(
        phi_s,
        1e23,
        1e-6
    )

    assert len(phi) == len(C)
    assert np.all(C > 0)

