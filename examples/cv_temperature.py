import numpy as np
import matplotlib.pyplot as plt
import os

from src.physics.moscap import (
    oxide_capacitance,
    semiconductor_capacitance,
    total_capacitance,
)
from src.physics.semiconductor import intrinsic_carrier_co, intrinsic_carrier_concentration

# Parameters
area = 1e-6          # m^2
N_A = 1e23           # doping (1/m^3)
C_ox = oxide_capacitance(area)

# Temperature range
temperatures = [200, 300, 400]

# Surface potential sweep
phi_s = np.linspace(0.01, 0.6, 100)

plt.figure()

for T in temperatures:

    ni = intrinsic_carrier_concentration(T)

    C_total = []

    for phi in phi_s:
        C_s = semiconductor_capacitance(phi, N_A, area)
        C = total_capacitance(C_ox, C_s)

        # simple temperature scaling (to show effect)
        C = C * (ni / intrinsic_carrier_concentration(300))

        C_total.append(C)

    plt.plot(phi_s, C_total, label=f"T = {T} K")

# Plot styling
plt.xlabel("Surface Potential (V)")
plt.ylabel("Capacitance (F)")
plt.title("Temperature-Dependent MOS C–V Characteristics")
plt.legend()
plt.grid()

# ---- Add here ----
BASE_DIR = os.path.dirname(os.path.dirname(__file__))
FIG_DIR = os.path.join(BASE_DIR, "figures")

os.makedirs(FIG_DIR, exist_ok=True)

# Save figure
plt.savefig(os.path.join(FIG_DIR, "intrinsic_carrier.png"), dpi=300)

plt.show()