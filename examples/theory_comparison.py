import os
import numpy as np
import matplotlib.pyplot as plt

BASE_DIR = os.path.dirname(os.path.dirname(__file__))

from src.physics.simulation import (
    compute_theory_comparison
)

# =====================================================
# Parameters
# =====================================================

area = 1e-6
N_A = 1e23

phi_s = np.linspace(0.01, 0.6, 200)

# =====================================================
# Theory vs Numerical Comparison
# =====================================================

phi_num, C_theory, C_num = compute_theory_comparison(
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