import numpy as np

from src.physics.poisson import solve_poisson_1d


def test_poisson_output_shape():
    """
    Output shape must match input shape.
    """

    rho = np.zeros(100)

    phi = solve_poisson_1d(
        rho=rho,
        dx=1e-9,
        epsilon=1e-11
    )

    assert len(phi) == len(rho)


def test_poisson_no_nan():
    """
    Poisson solution should not contain NaN values.
    """

    rho = np.ones(100)

    phi = solve_poisson_1d(
        rho=rho,
        dx=1e-9,
        epsilon=1e-11
    )

    assert not np.isnan(phi).any()