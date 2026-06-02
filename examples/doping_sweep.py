import sys
import os

BASE_DIR = os.path.dirname(os.path.dirname(__file__))
sys.path.append(BASE_DIR)

import numpy as np
import matplotlib.pyplot as plt

from src.physics.simulation import compute_doping_sweep

# =========================================================
# Parameters
# =========================================================

area = 1e-6

dopings = [
    1e21,
    1e22,
    1e23
]

phi_s = np.linspace(
    -0.5,
    1.0,
    300
)

# =========================================================
# Run simulation
# =========================================================

phi, results = compute_doping_sweep(
    phi_s,
    dopings,
    area
)

# =========================================================
# Plot results
# =========================================================

plt.figure(figsize=(6, 4))

for N_A, C in results.items():

    plt.plot(
        phi,
        C,
        label=f"N_A = {N_A:.0e} m⁻³"
    )

plt.xlabel("Surface Potential (V)")
plt.ylabel("Capacitance (F)")
plt.title("MOS C–V Curves for Different Doping Levels")

plt.grid()
plt.legend()

# =========================================================
# Save figure
# =========================================================

FIG_DIR = os.path.join(
    BASE_DIR,
    "figures"
)

os.makedirs(
    FIG_DIR,
    exist_ok=True
)

plt.tight_layout()

plt.savefig(
    os.path.join(
        FIG_DIR,
        "doping_sweep.png"
    ),
    dpi=150,
    bbox_inches="tight"
)

plt.show()