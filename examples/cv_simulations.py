import numpy as np
import os

from src.physics.simulation import (
    compute_cv_curve_advanced,
    plot_cv_curve,
)

# Parameters
area = 1e-6
N_A = 1e23

# Gate voltage range
Vg = np.linspace(-1, 2, 200)

# Compute
Vg_values, C = compute_cv_curve_advanced(Vg, N_A, area)

# Plot
plt = plot_cv_curve(Vg_values, C)

# Save
BASE_DIR = os.path.dirname(os.path.dirname(__file__))
FIG_DIR = os.path.join(BASE_DIR, "figures")

os.makedirs(FIG_DIR, exist_ok=True)

plt.savefig(os.path.join(FIG_DIR, "cv_curve.png"), dpi=150)
plt.show()