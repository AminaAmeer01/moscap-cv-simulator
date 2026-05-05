import numpy as np
import os

from src.physics.simulation import (
    compute_cv_vs_temperature,
    plot_cv_vs_temperature,
)

# Parameters
area = 1e-6
N_A = 1e23
temperatures = [200, 300, 400]

phi_s = np.linspace(0.01, 0.6, 100)

# Compute
phi, results = compute_cv_vs_temperature(phi_s, temperatures, N_A, area)

# Plot
plt = plot_cv_vs_temperature(phi, results)

# Save
BASE_DIR = os.path.dirname(os.path.dirname(__file__))
FIG_DIR = os.path.join(BASE_DIR, "figures")
os.makedirs(FIG_DIR, exist_ok=True)

plt.savefig(os.path.join(FIG_DIR, "cv_temperature.png"), dpi=150)
plt.show()