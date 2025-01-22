# Elijah Guess
# Quantum Circuit Simulation
# 1-22-2025

from qiskit.visualization import plot_histogram
from qiskit_aer.aerprovider import AerSimulator

# Simulate a quantum circuit using Qiskit's AerSimulator

def simulate_circuit(circuit):
    simulator = AerSimulator()
    result = simulator.run(circuit, shots=1024).result()
    return result.get_counts()

# Render a histogram of the simulation results

def render_histogram(counts):
    return plot_histogram(counts)
