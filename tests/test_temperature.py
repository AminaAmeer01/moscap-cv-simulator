import numpy as np
from src.physics.simulation import compute_cv_vs_temperature


def test_temperature_outputs():
    phi_s = np.linspace(0.01, 0.5, 50)
    temps = [200, 300]

    phi, results = compute_cv_vs_temperature(phi_s, temps, 1e23, 1e-6)

    assert len(results) == len(temps)


def test_temperature_scaling():
    phi_s = np.linspace(0.01, 0.5, 10)
    temps = [200, 400]

    _, results = compute_cv_vs_temperature(phi_s, temps, 1e23, 1e-6)

    C_low = results[200]
    C_high = results[400]

    # Higher temperature → higher intrinsic carriers → larger scaling
    assert any(c2 > c1 for c1, c2 in zip(C_low, C_high))