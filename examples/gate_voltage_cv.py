import sys
import os

BASE_DIR = os.path.dirname(os.path.dirname(__file__))
sys.path.append(BASE_DIR)

import numpy as np
import matplotlib.pyplot as plt

from src.physics.electrostatics import (
    approximate_surface_potential
)

from src.physics.simulation import (
    compute_cv_curve_advanced
)

# =========================================================
# Parameters
# =========================================================

area = 1e-6
N_A = 1e23

# Gate voltage sweep
Vg = np.linspace(-1, 2, 300)

# Convert gate voltage to surface potential
phi_s = approximate_surface_potential(Vg)

# Compute advanced MOS C-V
phi, C = compute_cv_curve_advanced(
    phi_s,
    N_A,
    area
)

# =========================================================
# Plot
# =========================================================

plt.figure(figsize=(6, 4))

plt.plot(Vg, C)

plt.xlabel("Gate Voltage (V)")
plt.ylabel("Capacitance (F)")

plt.title("MOS Capacitor C–V vs Gate Voltage")

plt.grid()

# =========================================================
# Save Figure
# =========================================================

FIG_DIR = os.path.join(BASE_DIR, "figures")

os.makedirs(FIG_DIR, exist_ok=True)

plt.tight_layout()

plt.savefig(
    os.path.join(FIG_DIR, "gate_voltage_cv.png"),
    dpi=150,
    bbox_inches="tight"
)

plt.show()