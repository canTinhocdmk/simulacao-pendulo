from src.simple_pendulum import simulate_simple_pendulum
from src.energy import calculate_energy
from src.plots import plot_time_series, plot_energy


def main():
    t, theta, omega = simulate_simple_pendulum(
        theta0=0.8,
        omega0=0.0,
        dt=0.01,
        t_max=10.0
    )

    kinetic, potential, total = calculate_energy(theta, omega)

    plot_time_series(t, theta, omega)
    plot_energy(t, kinetic, potential, total)

if __name__ == "__main__":
    main()