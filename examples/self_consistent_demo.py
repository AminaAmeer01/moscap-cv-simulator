import numpy as np
import matplotlib.pyplot as plt
import os

from src.physics.self_consistent_mos import solve_potential
from src.physics.semiconductor import intrinsic_carrier_concentration

# Parameters
N_A = 1e23
dx = 1e-9
ni = intrinsic_carrier_concentration(300)

# Initial guess
phi_initial = np.zeros(100)

# Solve
phi = solve_potential(
    phi_initial,
    dx,
    N_A,
    ni
)

# Plot
plt.figure(figsize=(5, 3))
x = np.arange(len(phi)) * dx * 1e9

plt.plot(x, phi)

plt.xlabel("Position (nm)")
plt.ylabel("Potential (V)")
plt.title("Self-Consistent Solution of Poisson Equation")
plt.grid()

# Save figure
BASE_DIR = os.path.dirname(os.path.dirname(__file__))
FIG_DIR = os.path.join(BASE_DIR, "figures")

os.makedirs(FIG_DIR, exist_ok=True)

plt.savefig(
    os.path.join(
        FIG_DIR,
        "self_consistent_potential.png"
    ),
    dpi=150,
    bbox_inches="tight"
)

plt.show()