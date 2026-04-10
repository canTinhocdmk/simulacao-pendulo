import matplotlib.pyplot as plt
import numpy as np
import os

os.makedirs("results/figures", exist_ok=True)

def plot_time_series(t, theta, omega):
    fig = plt.figure(figsize=(10, 5))
    plt.plot(t, theta, label="Ângulo 0(t)")
    plt.plot(t, omega, label="Velocidade angular w(t)")
    plt.xlabel("Tempo (s)")
    plt.ylabel("Valor")
    plt.title("Dinamica do pendulo simples")
    plt.legend()
    plt.grid(True)
    plt.tight_layout()
    plt.savefig("results/figures/time_series.png", dpi=300)
    return fig

def plot_energy(t, kinetic, potential, total, title="Energia do sistema"):
    fig = plt.figure(figsize=(10, 5))
    plt.plot(t, kinetic, label="Energia Cinética")
    plt.plot(t, potential, label="Energia Potencial")
    plt.plot(t, total, label="Energia Total")
    plt.xlabel("Tempo (s)")
    plt.ylabel("Energia (J)")
    plt.title(title)
    plt.legend()
    plt.grid(True)
    plt.tight_layout()
    plt.savefig("results/figures/energy.png", dpi=300)
    return fig

def plot_model_comparison(t, theta_lin, theta_nonlin):
    fig = plt.figure(figsize=(10, 5))
    plt.plot(t, theta_lin, label="Aproximação Linear", linestyle='--')
    plt.plot(t, theta_nonlin, label="Modelo Não-Linear")
    plt.xlabel("Tempo (s)")
    plt.ylabel("Ângulo (rad)")
    plt.title("Comparação Linear vs Não Linear")
    plt.legend()
    plt.grid(True)
    plt.tight_layout()
    return fig

def plot_trajectory(x, y, title="Trajetória da massa"):
    fig = plt.figure(figsize=(6, 6))
    plt.plot(x, y, label="Trajetória")
    plt.scatter(0, 0, color='red', marker='x', label="Pivô")
    plt.xlabel("x(m)")
    plt.ylabel("y(m)")
    plt.title(title)
    plt.legend()
    plt.grid(True)
    plt.axis("equal")
    plt.tight_layout()
    return fig

def plot_double_series(t, theta1, omega1, theta2, omega2):
    fig, ax = plt.subplots(figsize=(10, 4))
    ax.plot(t, theta1, label="01")
    ax.plot(t, theta2, label="02")
    ax.plot(t, omega1, label="w1", alpha=0.7)
    ax.plot(t, omega2, label="w2", alpha=0.7)
    ax.set_xlabel("tempo (s)")
    ax.set_ylabel("valor")
    ax.set_title("pendulo duplo")
    ax.grid(True)
    ax.legend()
    fig.tight_layout()
    return fig

def plot_snapshot(x1, y1, x2, y2, title="configuração final do sistema"):
    fig, ax = plt.subplots(figsize=(6, 6))
    ax.plot([0, x1], [0, y1], marker="o", color='blue')
    ax.plot([x1, x2], [y1, y2], marker="o", color='red')
    ax.set_title(title)
    ax.grid(True)
    ax.axis("equal")

    limit = max(1.2, np.max(np.abs([x1, y1, x2, y2])) + 0.5)
    ax.set_xlim(-limit, limit)
    ax.set_ylim(-limit, limit)
    fig.tight_layout()
    return fig