import numpy as np
import os

from src.physics.simulation import (
    compute_intrinsic_vs_temperature,
    plot_intrinsic_vs_temperature
)

# Temperature range
temperatures = np.linspace(200, 400, 100)

# Compute
T, ni = compute_intrinsic_vs_temperature(temperatures)

# Plot
plt = plot_intrinsic_vs_temperature(T, ni)

# Save path
BASE_DIR = os.path.dirname(os.path.dirname(__file__))
FIG_DIR = os.path.join(BASE_DIR, "figures")
os.makedirs(FIG_DIR, exist_ok=True)

plt.tight_layout()
plt.savefig(os.path.join(FIG_DIR, "intrinsic_carrier.png"), dpi=150)
plt.show()