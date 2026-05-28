import sys
import os

BASE_DIR = os.path.dirname(os.path.dirname(__file__))
sys.path.append(BASE_DIR)

import numpy as np
import matplotlib.pyplot as plt

from src.physics.poisson import solve_poisson_1d
from src.physics.constants import epsilon_si

# =====================================================
# Spatial grid
# =====================================================

N = 200

x = np.linspace(0, 1e-6, N)

dx = x[1] - x[0]

# =====================================================
# Charge density profile
# =====================================================

rho = np.zeros(N)

# Artificial depletion region
rho[70:130] = 1e-5

# =====================================================
# Solve Poisson equation
# =====================================================

phi = solve_poisson_1d(
    rho=rho,
    dx=dx,
    epsilon=epsilon_si
)

# =====================================================
# Plot
# =====================================================

plt.figure(figsize=(6, 4))

plt.plot(x * 1e6, phi)

plt.xlabel("Position (µm)")
plt.ylabel("Electrostatic Potential (V)")

plt.title("1D Numerical Poisson Solution")

plt.grid()

# =====================================================
# Save figure
# =====================================================

FIG_DIR = os.path.join(BASE_DIR, "figures")

os.makedirs(FIG_DIR, exist_ok=True)

plt.tight_layout()

plt.savefig(
    os.path.join(FIG_DIR, "poisson_solution.png"),
    dpi=150,
    bbox_inches="tight"
)

plt.show()