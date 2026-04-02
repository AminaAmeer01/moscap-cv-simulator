import numpy as np
import matplotlib.pyplot as plt
import imageio
import os

from src.physics.moscap import (
    oxide_capacitance,
    semiconductor_capacitance,
    total_capacitance
)

# Parameters
area = 1e-6
N_A = 1e23

voltages = np.linspace(0.01, 1, 100)
temperatures = [250, 275, 300, 325, 350]

os.makedirs("figures", exist_ok=True)

images = []

for T in temperatures:

    capacitance = []

    for V in voltages:

        phi_s = V   # simple approximation

        C_ox = oxide_capacitance(area)
        C_s = semiconductor_capacitance(phi_s, N_A, area)

        C_total = total_capacitance(C_ox, C_s)

        capacitance.append(C_total)

    plt.figure()
    plt.plot(voltages, capacitance)
    plt.xlabel("Voltage (V)")
    plt.ylabel("Capacitance (F)")
    plt.title(f"MOS C-V at {T} K")

    filename = f"figures/frame_{T}.png"
    plt.savefig(filename)
    plt.close()

    images.append(imageio.imread(filename))

imageio.mimsave("figures/cv_animation.gif", images, duration=0.8)

print("GIF saved to figures/cv_animation.gif")