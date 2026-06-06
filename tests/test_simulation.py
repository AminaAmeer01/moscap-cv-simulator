import numpy as np

from src.physics.simulation import (
    compute_doping_sweep,
    compute_tox_sweep,
    compute_gate_voltage_sweep,
    compute_theory_comparison,
    compute_error_analysis,
)


def test_doping_sweep_returns_results():
    """
    Doping sweep should return one result per doping value.
    """

    phi = np.linspace(-0.5, 1.0, 50)

    _, results = compute_doping_sweep(
        phi,
        [1e21, 1e22],
        1e-6
    )

    assert len(results) == 2


def test_tox_sweep_returns_results():
    """
    Oxide sweep should return one result per oxide thickness.
    """

    phi = np.linspace(-0.5, 1.0, 50)

    _, results = compute_tox_sweep(
        phi,
        [2e-9, 5e-9],
        1e-6
    )

    assert len(results) == 2


def test_gate_voltage_sweep_shape():
    """
    Gate-voltage sweep outputs should have matching sizes.
    """

    Vg = np.linspace(-1, 1, 50)

    V, C = compute_gate_voltage_sweep(
        Vg,
        1e23,
        1e-6
    )

    assert len(V) == len(C)


def test_theory_comparison_shapes():
    """
    Theory comparison outputs should have matching sizes.
    """

    phi = np.linspace(0.01, 1.0, 50)

    x, C_theory, C_num = compute_theory_comparison(
        phi,
        1e23,
        1e-6
    )

    assert len(x) == len(C_theory)
    assert len(x) == len(C_num)


def test_error_analysis_finite():
    """
    Error analysis metrics should be finite.
    """

    phi = np.linspace(0.01, 1.0, 50)

    (
        _,
        error,
        mean_error,
        max_error,
        rms_error
    ) = compute_error_analysis(
        phi,
        1e23,
        1e-6
    )

    assert np.all(np.isfinite(error))
    assert np.isfinite(mean_error)
    assert np.isfinite(max_error)
    assert np.isfinite(rms_error)