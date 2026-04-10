import numpy as np

def linear_derivatives(theta, omega, g, L):
    dtheta_dt = omega
    # Linear approximation: sin(theta) ~ theta
    domega_dt = -(g / L) * theta
    return dtheta_dt, domega_dt

def simulate_linear_pendulum(
    theta0=np.pi/4,
    omega0=0.0,
    L=1.0,
    g=9.81,
    dt=0.01,
    t_max=10.0
):
    n_steps = int(t_max / dt) + 1
    t = np.linspace(0, t_max, n_steps)

    theta = np.zeros(n_steps)
    omega = np.zeros(n_steps)
    
    theta[0] = theta0
    omega[0] = omega0

    for i in range(n_steps - 1):
        dtheta_dt, domega_dt = linear_derivatives(theta[i], omega[i], g=g, L=L)
        theta[i + 1] = theta[i] + dtheta_dt * dt
        omega[i + 1] = omega[i] + domega_dt * dt

    return theta, omega
