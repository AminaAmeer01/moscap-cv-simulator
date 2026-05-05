import numpy as np
import os

from src.physics.simulation import compute_cv_curve_advanced, plot_cv_curve

# Parameters
area = 1e-6
N_A = 1e23

# Surface potential range
phi_s = np.linspace(0.01, 0.6, 100)

# Compute (ADVANCED MODEL)
phi, C = compute_cv_curve_advanced(phi_s, N_A, area)

# Plot
plt = plot_cv_curve(phi, C)

# Save
BASE_DIR = os.path.dirname(os.path.dirname(__file__))
FIG_DIR = os.path.join(BASE_DIR, "figures")
os.makedirs(FIG_DIR, exist_ok=True)

plt.savefig(os.path.join(FIG_DIR, "cv_curve.png"), dpi=150)
plt.show()