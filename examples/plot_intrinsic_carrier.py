import numpy as np
import matplotlib.pyplot as plt

from src.physics.semiconductor import intrinsic_carrier_concentration

# Temperature range
T = np.linspace(200, 400, 100)

# Compute ni(T)
ni = [intrinsic_carrier_concentration(t) for t in T]

# Plot
plt.figure()
plt.plot(T, ni)
plt.xlabel("Temperature (K)")
plt.ylabel("Intrinsic Carrier Concentration (1/m^3)")
plt.title("Intrinsic Carrier Concentration vs Temperature")
plt.grid()

# Save figure
plt.savefig("figures/intrinsic_carrier.png", dpi=300)

plt.show()
