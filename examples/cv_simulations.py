import numpy as np
import matplotlib.pyplot as plt

from src.physics.moscap import (
    oxide_capacitance,
    semiconductor_capacitance,
    total_capacitance,
)

# Parameters
area = 1e-6          # m^2
N_A = 1e23           # doping (1/m^3)
C_ox = oxide_capacitance(area)

# Surface potential sweep (approximation)
phi_s = np.linspace(0.01, 0.6, 100)

C_total = []

for phi in phi_s:
    C_s = semiconductor_capacitance(phi, N_A, area)
    C = total_capacitance(C_ox, C_s)
    C_total.append(C)

# Plot
plt.figure(figsize=(4.5,3))
plt.plot(phi_s, C_total)
plt.xlabel("Surface Potential (V)")
plt.ylabel("Capacitance (F)")
plt.title("MOS Capacitor C–V Curve (Simplified)")
plt.grid()

# Save figure
plt.tight_layout()
plt.savefig("figures/cv_curve.png", dpi=150, bbox_inches="tight")

plt.show()
