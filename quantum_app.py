# Elijah Guess
# Quantum Circuit Simulation
# 1-22-2025

import streamlit as st
from circuits import create_circuit, qft_circuit
from teleportation import quantum_teleportation
from utils import simulate_circuit, render_histogram
import matplotlib.pyplot as plt

# Global Title

st.title("Quantum Circuit Simulator")

# Global Sidebar

st.sidebar.header("Choose a Quantum Circuit")
circuit_option = st.sidebar.selectbox(
    "Select Circuit",
    ["Basic Circuit", "Quantum Teleportation", "Quantum Fourier Transform (QFT)"]
)
num_qubits = st.sidebar.slider("Number of Qubits", 2, 5, 3)

# Function to display content for the selected circuit

def display_page(circuit, description, equations):

    # Selected Circuit Description

    st.write("### Description")
    st.write(description)

    # Selected LaTeX Equations

    st.write("### Mathematical Equations")
    for eq in equations:
        st.latex(eq)

    # Selected Quantum Circuit

    st.write("### Quantum Circuit")
    fig = plt.figure()
    ax = fig.add_subplot(111)
    circuit.draw(output="mpl", ax=ax)
    st.pyplot(fig)

    # Selected Results

    st.write("### Simulation Results")
    counts = simulate_circuit(circuit)
    fig = render_histogram(counts)
    st.pyplot(fig)

# Circuit Selections

if circuit_option == "Basic Circuit":
    circuit = create_circuit(num_qubits)
    description = r"""
        The Basic Circuit demonstrates simple quantum operations. The Hadamard gate $H$ creates superposition, 
        and the Pauli-X gate $X$ flips the state of a qubit.

        When running a basic quantum circuit, measurements are performed on the qubits, and the result 
        is represented as a probability distribution of the qubit states. In quantum computing, after 
        applying quantum gates like Hadamard or Pauli-X, the qubit is in a superposition of states. 
        When measured, it collapses to one of the computational basis states, with a certain probability.

        The quantum circuit and state probability histogram are displayed below.
    """
    equations = [
        r"H|0\rangle = \frac{1}{\sqrt{2}}(|0\rangle + |1\rangle)",
        r"X|0\rangle = |1\rangle \quad \text{and} \quad X|1\rangle = |0\rangle"
    ]
    display_page(circuit, description, equations)

elif circuit_option == "Quantum Teleportation":
    circuit = quantum_teleportation()
    description = r"""
        Quantum Teleportation transfers a quantum state | $\psi$ $\rangle$ = $\alpha$ | 0 $\rangle$ + $\beta$ | 1 $\rangle$ 
        using entanglement and classical communication between two parties.

        In quantum teleportation, the key goal is to transmit the quantum state of a qubit (without physically sending it). 
        The measurement outcomes in this case will reflect the classical bits that Alice sends to Bob, along with 
        the state that Bob reconstructs.

        The quantum circuit and state probability histogram are displayed below.
    """
    equations = [
        r"|\psi\rangle \otimes |00\rangle = (\alpha|0\rangle + \beta|1\rangle) \otimes |00\rangle",
        r"|\Phi\rangle = \frac{1}{\sqrt{2}} \left( |0\rangle|00\rangle + |1\rangle|10\rangle \right)"
    ]
    st.write("This circuit always uses 3 qubits for teleportation.")
    display_page(circuit, description, equations)

elif circuit_option == "Quantum Fourier Transform (QFT)":
    circuit = qft_circuit(num_qubits)
    description = r"""
        The Quantum Fourier Transform (QFT) applies a quantum equivalent of the discrete Fourier transform. 
        It converts the input quantum state into the Fourier basis.
        
        After applying the QFT, the quantum state is transformed into a superposition of frequency components.

        The quantum circuit and state probability histogram are displayed below.
    """
    equations = [
        r"QFT|\psi\rangle = \frac{1}{\sqrt{N}} \sum_{k=0}^{N-1} \left( \sum_{x=0}^{N-1} a_x e^{2\pi i xk / N} \right)|k\rangle",
        r"|j\rangle \to \frac{1}{\sqrt{2^n}} \sum_{k=0}^{2^n - 1} e^{2\pi i j k / 2^n} |k\rangle"
    ]
    display_page(circuit, description, equations)
