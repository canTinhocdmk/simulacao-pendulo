import numpy as np
from scipy.integrate import solve_ivp

def double_pendulum_derivatives(t, y, m1, m2, L1, L2, g):
    theta1, omega1, theta2, omega2 = y

    delta = theta2 - theta1

    den1 = (m1 + m2) * L1 - m2 *L1 * np.cos(delta)**2
    den2 = (L2/L1) * den1

    dtheta_dt = omega1
    dtheta2_dt = omega2

    domega_dt = (
        m2 * L1 * omega1**2 * np.sin(delta) * np.cos(delta)
        + m2 * g * np.sin(theta2) * np.cos(delta)
        + m2 * L2 * omega2**2 * np.sin(delta)
        - (m1 + m2) * g * np.sin(theta1)
    ) /den1

    domega2_dt = (
        -m2 * L2 * omega2**2 * np.sin(delta) * np.cos(delta)
        + (m1 + m2) *(
            g * np.sin(theta1) * np.cos(delta)
            - L1 * omega1**2 * np.sin(delta)
            -g * np.sin(theta2)

        )
    ) /den2

    return [dtheta_dt, domega_dt, dtheta2_dt, domega2_dt]
def simulate_double_pendulum(
    theta1_0 = np.pi /2,
    omega1_0 = 0.0,
    theta2_0 = np.pi /2,
    omega2_0 = 0.0,
    m1 = 1.0,
    m2 = 1.0,
    L1 = 1.0,
    L2 = 1.0,
    g = 9.81,
    t_max = 20.0,
    dt = 0.01
):
    t_eval = np.arange(0, t_max + dt, dt)
    
    y0 = [theta1_0, omega1_0, theta2_0, omega2_0]
    sol = solve_ivp(
        double_pendulum_derivatives,
        [0, t_max],
        y0,
        t_eval = t_eval,
        args = (m1, m2, L1, L2, g),
        rtol = 1e-8,
        atol = 1e-8
    )
    theta1 = sol.y[0]
    omega1 = sol.y[1]
    theta2 = sol.y[2]
    omega2 = sol.y[3]

    return sol.t, theta1, omega1, theta2, omega2

def calculate_energy(theta1, omega1, theta2, omega2, m1, m2, L1, L2, g):
    v1_sq = (L1 * omega1) ** 2
    
    v2_sq = (
        v1_sq
        + (L2 * omega2) ** 2
        + 2 * L1 * L2 * omega1 * omega2 * np.cos(theta1 - theta2)
    )
    kinetic = 0.5 *m1 * v1_sq + 0.5 *m2 * v2_sq

    potential = (
        -(m1 + m2) * g * L1 * np.cos(theta1)
        - m2 * g * L2 * np.cos(theta2)

    )
    total = kinetic + potential
    return kinetic, potential, total

def get_positions(theta1, theta2, L1, L2):
    x1 = L1 * np.sin(theta1)
    y1 = -L1 * np.cos(theta1)
    x2 = x1 + L2 * np.sin(theta2)
    y2 = y1 - L2 * np.cos(theta2)
    return x1, y1, x2, y2            
            