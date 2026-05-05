import numpy as np
from src.physics.simulation import compute_cv_curve


def test_cv_output_shape():
    phi_s = np.linspace(0.01, 0.5, 50)
    phi, C = compute_cv_curve(phi_s, 1e23, 1e-6)

    assert len(phi) == len(C)


def test_capacitance_positive():
    phi_s = np.linspace(0.01, 0.5, 10)
    _, C = compute_cv_curve(phi_s, 1e23, 1e-6)

    assert all(c > 0 for c in C)