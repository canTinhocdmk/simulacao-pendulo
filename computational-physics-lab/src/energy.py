import numpy as np

def calculate_energy(theta, omega, m=1.0, g=9.81, L=1.0):
    kinetic = 0.5 *m * (L *omega) ** 2
    potential = m * g * L * (1 - np.cos(theta))
    total = kinetic + potential
    return kinetic, potential, total