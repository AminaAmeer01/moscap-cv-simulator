import numpy as np
import matplotlib.pyplot as plt
import os

from src.physics.semiconductor import intrinsic_carrier_concentration

# Temperature range
T = np.linspace(200, 400, 100)

# Compute ni(T)
ni = [intrinsic_carrier_concentration(t) for t in T]

# Plot
plt.figure(figsize=(5,3))
plt.plot(T, ni)
plt.xlabel("Temperature (K)")
plt.ylabel("Intrinsic Carrier Concentration (1/m^3)")
plt.title("Intrinsic Carrier Concentration vs Temperature")
plt.grid()

# ---- Add here ----
BASE_DIR = os.path.dirname(os.path.dirname(__file__))
FIG_DIR = os.path.join(BASE_DIR, "figures")

os.makedirs(FIG_DIR, exist_ok=True)

# Save figure
plt.savefig(os.path.join(FIG_DIR, "intrinsic_carrier.png"), dpi=150)

plt.show()
