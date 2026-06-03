import sys
import os

BASE_DIR = os.path.dirname(os.path.dirname(__file__))
sys.path.append(BASE_DIR)

import numpy as np
import matplotlib.pyplot as plt

from src.physics.simulation import compute_tox_sweep

# =========================================================
# Parameters
# =========================================================

area = 1e-6
N_A = 1e23

tox_values = [2e-9, 5e-9, 10e-9]

phi_s = np.linspace(0.01, 0.6, 300)

# =========================================================
# Run simulation
# =========================================================

phi, results = compute_tox_sweep(
    phi_s,
    tox_values,
    area,
    N_A
)

# =========================================================
# Plot
# =========================================================

plt.figure(figsize=(6, 4))

for tox, C in results.items():

    plt.plot(
        phi,
        C,
        label=f"t_ox = {tox * 1e9:.0f} nm"
    )

# =========================================================
# Styling
# =========================================================

plt.xlabel("Surface Potential (V)")
plt.ylabel("Capacitance (F)")
plt.title("Effect of Oxide Thickness on MOS C–V")

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
        "tox_sweep.png"
    ),
    dpi=150,
    bbox_inches="tight"
)

plt.show()