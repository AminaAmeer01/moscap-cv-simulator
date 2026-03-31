# MOSCAP C–V Simulator

# MOSCAP C–V Simulator

![Python](https://img.shields.io/badge/Python-3.9+-blue)
![Physics](https://img.shields.io/badge/Physics-Semiconductor-green)
![Simulation](https://img.shields.io/badge/Simulation-MOSCAP-orange)
![Status](https://img.shields.io/badge/Status-Research%20Project-purple)

A scientific Python project for simulating **Capacitance–Voltage (C–V) characteristics** of a Metal-Oxide Semiconductor (MOS) capacitor, including **temperature-dependent semiconductor effects**.

This project is designed with research level clarity, modular physics implementation, and reproducible numerical simulations.

---

## Project Overview
![MOSCAP Simulation](figures/readme_style.png)

---

##  Features

- **Oxide capacitance** calculation
- **Semiconductor depletion capacitance** modeling
- Simulate **total MOS capacitance (series combination)**
- **temperature dependent** intrinsic carrier concentration
- Modular physics-based implementation
- Scientific visualization of MOS behaviour
### Generated Plots:
  - Intrinsic carrier concentration vs temperature
  - C–V characteristics at fixed temperature
  - C–V curves at multiple temperatures

---

## Project Structure

```
moscap-cv-simulator/
│
├── src/                 # Core physics modules
│   └── physics/
│       ├── moscap.py
│       ├── semiconductor.py
│       └── constants.py
│
├── examples/            # Simulation scripts
│   ├── cv_simulations.py
│   ├── cv_temperature.py
│   └── plot_intrinsic_carrier.py
│
├── tests/               # Unit tests
│   └── test_moscap.py
│
├── requirements.txt
└── README.md
```

---

##  Installation

### Clone the repository:

```bash
git clone https://github.com/YOUR_USERNAME/moscap-cv-simulator.git
cd moscap-cv-simulator
````

### Create virtual environment:

```bash
python -m venv venv
```
### Activate environment
##### Linux/Mac
```bash
source venv/bin/activate
````
##### windows
```bash
venv\Scripts\activate
````
### Install dependencies
```bash
pip install -r requirements.txt
````

## How to Run

### Intrinsic carrier concentration
```bash
python examples/plot_intrinsic_carrier.py
```
### Basic C–V simulation
```bash
python examples/cv_simulations.py
````
### Temperature-dependent C-V curves
```bash
python examples/cv_temperature.py
````
## Running Tests
```bash
pytest
```
#### Expected output:
5 passed

## Physics Background

The MOS capacitor is modeled using standard semiconductor physics.

### Oxide Capacitance

$$
C_{ox} = \frac{\varepsilon_{ox} A}{t_{ox}}
$$

where:

- εₒₓ — oxide permittivity  
- A — capacitor area  
- tₒₓ — oxide thickness

### Semiconductor Depletion Width
$$
W = \sqrt{\frac{2 \varepsilon_s \phi_s}{q N_A}}
$$
where:

- εₛ — semiconductor permittivity
- ϕₛ — surface potential
- q — electron charge
- Nₐ — doping concentration

### Semiconductor Capacitance
$$
C_s = \frac{\varepsilon_s A}{W}
$$

where:

- εₛ — semiconductor permittivity
- A — capacitor area
- W — depletion width

### Total MOS Capacitance (series combination)
$$
\frac{1}{C} = \frac{1}{C_{ox}} + \frac{1}{C_s}
$$

where:
- C — total capacitance
- Cₒₓ — oxide capacitance
- Cₛ — semiconductor capacitance

### Intrinsic Carrier Concentration (temperature_dependent)
$$
n_i(T) = n_{i,300K}
\left(\frac{T}{300}\right)^{3/2}
\exp\left[
-\frac{E_g}{2k_B}
\left(
\frac{1}{T} - \frac{1}{300}
\right)
\right]
$$

where:

- nᵢ(T) — intrinsic carrier concentration
- T — temperature (Kelvin)
- E_g — bandgap energy
- k_B — Boltzmann constant

## Simulation Results

### Intrinsic Carrier Concentration vs Temperature

This plot shows the exponential increase of intrinsic carrier concentration with temperature.

![Intrinsic Carrier](figures/intrinsic_carrier.png)
---

### C–V Curve at Fixed Temperature

The MOS capacitor exhibits depletion region behaviour as expected.

![C-V Simulation](figures/cv_curve.png)
---

### Temperature Dependent C-V Curves

Temperature affects depletion width and total capaciatnce.

![Temperature](figures/cv_temperature.png)
---

## Model Assumptions

- Ideal MOS capacitor
- No interface traps
- No oxide charge
- Uniform doping
- Quasi-static capacitance model

## Numerical Implementation
The simulator uses:

- NumPy for numerical calculations
- Matplotlib for plotting
- Modular physics functions
- Scientific reproducibility

## Example Outputs
The simulator generates:

- Exponential increase of intrinsic carrier concentration with temperature
- Depletion-region C-V behaviour
- Temperature-dependent capacitance curves

## Design Principles

- Modular architecture
- Separation of physics and simulation scripts
- No hardcoded paths
- Testable scientific functions
- Minimal dependencies (numpy, matplotlib)

## Limitations
 - Ideal MOS approximation
 - No inversion regime modeling
 - No interface traps
 - Simplified temperature dependence
 - 
## Possible Extensions

- Flat-band voltage modeling
- Interface trap capacitance
- Full inversion modeling
- Experimental data fitting
- TCAD-level simulation extension

## License
MIT License

## Author
Syeda Amina Ameer

Master's in Physics - Materaial Physics & Nanoscience

University of Bologna
