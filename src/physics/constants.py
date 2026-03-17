"""
Physical constants for semiconductor MOS capacitor simulations.
All units are SI unless otherwise noted.
"""

# Fundamental constants
q = 1.602176634e-19       # Elementary charge, C
k_B = 1.380649e-23        # Boltzmann constant, J/K
epsilon_0 = 8.854187817e-12  # Vacuum permittivity, F/m

# Silicon properties
epsilon_si = 11.7 * epsilon_0  # Relative permittivity of silicon
ni_300K = 1.45e16               # Intrinsic carrier concentration at 300K, 1/m^3
Eg_300K = 1.12                  # Silicon bandgap at 300K, eV

# Oxide properties
epsilon_ox = 3.9 * epsilon_0    # SiO2 permittivity
tox_default = 5e-9               # Default oxide thickness, m
