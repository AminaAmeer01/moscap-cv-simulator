import sys
import os

BASE_DIR = os.path.dirname(os.path.dirname(__file__))
sys.path.append(BASE_DIR)

import numpy as np
import matplotlib.pyplot as plt

from src.physics.simulation import compute_cv_curve_advanced

# =========================================================
# Parameters
# =========================================================

area = 1e-6

# Different doping concentrations
dopings = [1e21, 1e22, 1e23]

# Surface potential range
phi_s = np.linspace(-0.5, 1.0, 300)

# =========================================================
# Figure setup
# =========================================================

plt.figure(figsize=(6, 4))

# =========================================================
# Run simulations
# =========================================================

for N_A in dopings:

    phi, C = compute_cv_curve_advanced(
        phi_s,
        N_A,
        area
    )

    plt.plot(
        phi,
        C,
        label=f"N_A = {N_A:.0e} m⁻³"
    )

# =========================================================
# Plot styling
# =========================================================

plt.xlabel("Surface Potential (V)")
plt.ylabel("Capacitance (F)")
plt.title("MOS C–V Curves for Different Doping Levels")

plt.grid()
plt.legend()

# =========================================================
# Save figure
# =========================================================

BASE_DIR = os.path.dirname(os.path.dirname(__file__))

FIG_DIR = os.path.join(BASE_DIR, "figures")

os.makedirs(FIG_DIR, exist_ok=True)

plt.tight_layout()

plt.savefig(
    os.path.join(FIG_DIR, "doping_sweep.png"),
    dpi=150,
    bbox_inches="tight"
)

plt.show()