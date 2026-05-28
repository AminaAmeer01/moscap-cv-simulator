import sys
import os

BASE_DIR = os.path.dirname(os.path.dirname(__file__))
sys.path.append(BASE_DIR)

import numpy as np
import matplotlib.pyplot as plt

from src.physics.moscap import (
    oxide_capacitance,
    semiconductor_capacitance,
    total_capacitance
)

from src.physics.simulation import (
    compute_cv_curve_advanced
)

# =====================================================
# Parameters
# =====================================================

area = 1e-6
N_A = 1e23

phi_s = np.linspace(0.01, 0.6, 200)

# =====================================================
# Analytical Model
# =====================================================

C_ox = oxide_capacitance(area)

C_theory = []

for phi in phi_s:

    C_s = semiconductor_capacitance(
        phi,
        N_A,
        area
    )

    C_total = total_capacitance(
        C_ox,
        C_s
    )

    C_theory.append(C_total)

# =====================================================
# Numerical / Advanced Model
# =====================================================

phi_num, C_num = compute_cv_curve_advanced(
    phi_s,
    N_A,
    area
)

# =====================================================
# Plot
# =====================================================

plt.figure(figsize=(6, 4))

plt.plot(
    phi_s,
    C_theory,
    label="Analytical Theory",
    linewidth=2
)

plt.plot(
    phi_num,
    C_num,
    '--',
    label="Numerical Simulation",
    linewidth=2
)

plt.xlabel("Surface Potential (V)")
plt.ylabel("Capacitance (F)")

plt.title("Analytical vs Numerical MOS C–V")

plt.legend()

plt.grid()

# =====================================================
# Save
# =====================================================

FIG_DIR = os.path.join(BASE_DIR, "figures")

os.makedirs(FIG_DIR, exist_ok=True)

plt.tight_layout()

plt.savefig(
    os.path.join(FIG_DIR, "theory_comparison.png"),
    dpi=150,
    bbox_inches="tight"
)

plt.show()