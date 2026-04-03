import numpy as np
import matplotlib.pyplot as plt
import imageio.v2 as imageio
import os

from src.physics.moscap import (
    oxide_capacitance,
    semiconductor_capacitance,
    total_capacitance
)

# Get project root directory
BASE_DIR = os.path.dirname(os.path.dirname(__file__))
FIGURES_DIR = os.path.join(BASE_DIR, "figures")

os.makedirs(FIGURES_DIR, exist_ok=True)

# Parameters
area = 1e-6
N_A = 1e23

voltages = np.linspace(0.01, 1, 100)
temperatures = [200, 250, 300, 350, 400]

os.makedirs("figures", exist_ok=True)

images = []

for T in temperatures:

    capacitance = []

    for V in voltages:
        phi_s = V * (T / 300)

        C_ox = oxide_capacitance(area)
        C_s = semiconductor_capacitance(phi_s, N_A, area)

        C_total = total_capacitance(C_ox, C_s)

        capacitance.append(C_total)

    plt.figure()
    plt.plot(voltages, capacitance)
    plt.xlabel("Voltage (V)")
    plt.ylabel("Capacitance (F)")
    plt.title(f"MOS C-V at {T} K")

    filename = os.path.join(FIGURES_DIR, f"frame_{T}.png")
    plt.savefig(filename)
    plt.close()

    images.append(imageio.imread(filename))

gif_path = os.path.join(FIGURES_DIR, "cv_animation.gif")
imageio.mimsave(gif_path, images, duration=1.5)

print("GIF saved to figures/cv_animation.gif")