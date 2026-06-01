import sys
import os

BASE_DIR = os.path.dirname(os.path.dirname(__file__))
sys.path.append(BASE_DIR)

import numpy as np
import matplotlib.pyplot as plt

from src.physics.poisson import solve_poisson_1d

rho = np.ones(100)

dx = 1e-9
epsilon = 11.7 * 8.854e-12

phi = solve_poisson_1d(
    rho,
    dx,
    epsilon
)

plt.figure(figsize=(5,3))
plt.plot(phi)

plt.xlabel("Grid Point")
plt.ylabel("Potential (V)")
plt.title("1D Poisson Solver Demonstration")
plt.grid()

BASE_DIR = os.path.dirname(os.path.dirname(__file__))
FIG_DIR = os.path.join(BASE_DIR, "figures")

os.makedirs(FIG_DIR, exist_ok=True)

plt.savefig(
    os.path.join(
        FIG_DIR,
        "poisson_potential.png"
    ),
    dpi=150
)

plt.show()