import sys
import os

BASE_DIR = os.path.dirname(os.path.dirname(__file__))
sys.path.append(BASE_DIR)

import numpy as np
import matplotlib.pyplot as plt

from src.physics.simulation import (
    compute_error_analysis
)

# =====================================================
# Parameters
# =====================================================

area = 1e-6

N_A = 1e23

phi_s = np.linspace(
    0.01,
    0.6,
    200
)

# =====================================================
# Run analysis
# =====================================================

(
    phi,
    relative_error,
    mean_error,
    max_error,
    rms_error
) = compute_error_analysis(
    phi_s,
    N_A,
    area
)

# =====================================================
# Print metrics
# =====================================================

print(
    "Mean Relative Error :",
    mean_error
)

print(
    "Maximum Relative Error :",
    max_error
)

print(
    "RMS Relative Error :",
    rms_error
)

# =====================================================
# Figures directory
# =====================================================

FIG_DIR = os.path.join(
    BASE_DIR,
    "figures"
)

os.makedirs(
    FIG_DIR,
    exist_ok=True
)

# =====================================================
# Save metrics
# =====================================================

with open(
    os.path.join(
        FIG_DIR,
        "error_metrics.txt"
    ),
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

plt.figure(
    figsize=(6, 4)
)

plt.plot(
    phi,
    relative_error,
    linewidth=2
)

plt.xlabel(
    "Surface Potential (V)"
)

plt.ylabel(
    "Relative Error"
)

plt.title(
    "Relative Error: Numerical vs Analytical"
)

plt.grid()

plt.tight_layout()

# =====================================================
# Save figure
# =====================================================

plt.savefig(
    os.path.join(
        FIG_DIR,
        "relative_error.png"
    ),
    dpi=150,
    bbox_inches="tight"
)

plt.show()