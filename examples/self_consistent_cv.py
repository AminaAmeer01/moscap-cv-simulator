import numpy as np
import matplotlib.pyplot as plt

from src.physics.self_consistent_mos import compute_self_consistent_cv

Vg = np.linspace(-1, 2, 50)

V, C = compute_self_consistent_cv(Vg, N_A=1e23, ni=1e16)

plt.plot(V, C)
plt.xlabel("Gate Voltage")
plt.ylabel("Capacitance")
plt.title("Self-Consistent MOS C-V")
plt.grid()

plt.show()