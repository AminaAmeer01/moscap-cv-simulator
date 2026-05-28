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
# Analytical solution
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

C_theory = np.array(C_theory)

# =====================================================
# Numerical solution
# =====================================================

phi_num, C_num = compute_cv_curve_advanced(
    phi_s,
    N_A,
    area
)

# =====================================================
# Relative error
# =====================================================

relative_error = np.abs(
    (C_num - C_theory) / C_theory
)

# =====================================================
# Error metrics
# =====================================================

mean_error = np.mean(relative_error)

max_error = np.max(relative_error)

rms_error = np.sqrt(
    np.mean(relative_error**2)
)

print("Mean Relative Error :", mean_error)

print("Maximum Relative Error :", max_error)

print("RMS Relative Error :", rms_error)

# =====================================================
# Figures directory
# =====================================================

FIG_DIR = os.path.join(BASE_DIR, "figures")

os.makedirs(FIG_DIR, exist_ok=True)

# =====================================================
# Save numerical metrics
# =====================================================

with open(
    os.path.join(FIG_DIR, "error_metrics.txt"),
    "w"
) as f:

    f.write(
        f"Mean Relative Error: {mean_error}\n"
    )

    f.write(
        f"Maximum Relative Error: {max_error}\n"
    )

    f.write(
        f"RMS Relative Error: {rms_error}\n"
    )

# =====================================================
# Plot
# =====================================================

plt.figure(figsize=(6, 4))

plt.plot(
    phi_s,
    relative_error,
    linewidth=2
)

plt.xlabel("Surface Potential (V)")

plt.ylabel("Relative Error")

plt.title("Relative Error: Numerical vs Analytical")

plt.grid()

plt.tight_layout()

# =====================================================
# Save figure
# =====================================================

plt.savefig(
    os.path.join(FIG_DIR, "relative_error.png"),
    dpi=150,
    bbox_inches="tight"
)

plt.show()