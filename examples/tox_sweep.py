import sys
import os

BASE_DIR = os.path.dirname(os.path.dirname(__file__))
sys.path.append(BASE_DIR)

import numpy as np
import matplotlib.pyplot as plt

from src.physics.moscap import (
    semiconductor_capacitance,
    total_capacitance,
    oxide_capacitance,
)

# =========================================================
# Parameters
# =========================================================

area = 1e-6
N_A = 1e23

# Different oxide thicknesses (meters)
tox_values = [2e-9, 5e-9, 10e-9]

# Surface potential range
phi_s = np.linspace(0.01, 0.6, 300)

# =========================================================
# Plot setup
# =========================================================

plt.figure(figsize=(6, 4))

# =========================================================
# Simulations
# =========================================================

for tox in tox_values:

    # Compute oxide capacitance
    C_ox = oxide_capacitance(area, tox)

    C_total = []

    for phi in phi_s:

        C_s = semiconductor_capacitance(
            phi,
            N_A,
            area
        )

        C = total_capacitance(C_ox, C_s)

        C_total.append(C)

    plt.plot(
        phi_s,
        C_total,
        label=f"t_ox = {tox*1e9:.0f} nm"
    )

# =========================================================
# Plot styling
# =========================================================

plt.xlabel("Surface Potential (V)")
plt.ylabel("Capacitance (F)")
plt.title("Effect of Oxide Thickness on MOS C–V")

plt.grid()
plt.legend()

# =========================================================
# Save figure
# =========================================================

FIG_DIR = os.path.join(BASE_DIR, "figures")

os.makedirs(FIG_DIR, exist_ok=True)

plt.tight_layout()

plt.savefig(
    os.path.join(FIG_DIR, "tox_sweep.png"),
    dpi=150,
    bbox_inches="tight"
)

plt.show()