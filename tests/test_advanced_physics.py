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