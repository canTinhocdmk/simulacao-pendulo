import numpy as np
import streamlit as st

from src.simple_pendulum import simulate_simple_pendulum
from src.linear_vs_nonlinear import simulate_linear_pendulum
from src.energy import calculate_energy
from src.double_pendulum import (
    simulate_double_pendulum,
    calculate_energy as calculate_energy_double,
    get_positions,
)

from src.plots import (
    plot_time_series,
    plot_energy,
    plot_model_comparison,
    plot_trajectory,
    plot_double_series,
    plot_snapshot,
)


st.set_page_config(page_title="lab pendulo", layout="wide")

st.title("Laboratório de Física")
st.subheader("Simulador de Pêndulo")

mode = st.sidebar.selectbox("Escolha o tipo de pêndulo", ["Simples", "Duplo"])

st.sidebar.markdown("---")
st.sidebar.write("Parâmetros Gerais")
g = st.sidebar.number_input("Gravidade g", value = 9.81, step = 0.1)
dt = st.sidebar.number_input("Passo de tempo dt", value = 0.01, step = 0.01, format = "%.4f")
t_max = st.sidebar.number_input("Tempo máximo", value = 10.0, step = 1.0)

if mode == "Simples":
    st.sidebar.markdown("### Parâmetros do pêndulo simples")
    theta0 = st.sidebar.number_input("Ângulo inicial theta0 (rad)", value = 0.8, step = 0.1)
    omega0 = st.sidebar.number_input("Velocidade inicial omega0", value = 0.0, step = 0.1)
    L = st.sidebar.number_input("Comprimento L", value = 1.0, step = 0.1)
    m = st.sidebar.number_input("Massa m", value = 1.0, step = 0.1)

    run = st.sidebar.button("Simular")

    if run:
        t, theta, omega = simulate_simple_pendulum(
            theta0 = theta0,
            omega0 = omega0,
            L = L,
            g = g,
            t_max = t_max,
            dt = dt
        )
        theta_lin, omega_lin = simulate_linear_pendulum(
            theta0 = theta0,
            omega0 = omega0,
            L = L,
            g = g,
            t_max = t_max,
            dt = dt
        )
        
        kinetic, potential, total = calculate_energy(theta, omega, m=m, g=g, L=L)
        x = L * np.sin(theta)
        y = -L * np.cos(theta)

        col1, col2 = st.columns(2)
        with col1:
            st.pyplot(plot_time_series(t, theta, omega))
            st.pyplot(plot_model_comparison(t, theta_lin, theta))
            
        with col2:
            st.pyplot(plot_energy(t, kinetic, potential, total, title = "Energia do sistema simples"))
            st.pyplot(plot_trajectory(x, y, title = "Trajetória da massa"))

            st.markdown("### Interpretação")

            st.write(
                """
                O modelo não linear usa a função sin(theta) completa,
                já o modelo linear usa a aproximação sin(theta) = theta.
                Para ângulos pequenos as duas soluções se aproximam,
                mas para ângulos maiores a divergência cresce.
                """
            )

else:
    st.sidebar.markdown("### Parâmetros do pêndulo duplo")
    theta1_0 = st.sidebar.number_input("Ângulo inicial theta1 (rad)", value = 1.2, step = 0.1)
    omega1_0 = st.sidebar.number_input("Velocidade inicial w1", value = 0.0, step = 0.1)
    theta2_0 = st.sidebar.number_input("Ângulo inicial theta2 (rad)", value = 1.0, step = 0.1)
    omega2_0 = st.sidebar.number_input("Velocidade inicial w2", value = 0.0, step = 0.1)

    L1 = st.sidebar.number_input("Comprimento L1", value = 1.0, step = 0.1)
    L2 = st.sidebar.number_input("Comprimento L2", value = 1.0, step = 0.1)
    m1 = st.sidebar.number_input("Massa m1", value = 1.0, step = 0.1)
    m2 = st.sidebar.number_input("Massa m2", value = 1.0, step = 0.1)
    run = st.sidebar.button("Simular")

    if run:
        t, theta1, omega1, theta2, omega2 = simulate_double_pendulum(
            theta1_0 = theta1_0,
            omega1_0 = omega1_0,
            theta2_0 = theta2_0,
            omega2_0 = omega2_0,
            m1 = m1,
            m2 = m2,
            L1 = L1,
            L2 = L2,
            g = g,
            t_max = t_max,
            dt = dt
        )
        kinetic, potential, total = calculate_energy_double(
            theta1, omega1, theta2, omega2, m1, m2, L1, L2, g
        )
        x1, y1, x2, y2 = get_positions(theta1, theta2, L1, L2)

        col1, col2 = st.columns(2)

        with col1:
            st.pyplot(plot_double_series(t, theta1, omega1, theta2, omega2))
            st.pyplot(plot_snapshot(x1[-1], y1[-1], x2[-1], y2[-1], title = "Configuração final"))

        with col2:
            st.pyplot(plot_energy(t, kinetic, potential, total, title = "Energia do pêndulo duplo"))
            st.pyplot(plot_trajectory(x2, y2, title = "Trajetória da segunda massa"))

            st.markdown("### Interpretação")
            st.write(
                """
                O pêndulo duplo é um sistema caótico.
                Pequenas mudanças iniciais podem gerar grandes diferenças no futuro.
                Isso o torna um problema clássico da dinâmica do caos,
                assim como o famoso problema da borboleta e o dos três corpos.
                """
            )