# Elijah Guess
# Quantum Circuit Simulation
# 1-22-2025

from qiskit import QuantumCircuit
import numpy as np

# Implement a basic quantum circuit with Hadamard and CNOT gates

def create_circuit(num_qubits: int):
    circuit = QuantumCircuit(num_qubits)
    for i in range(num_qubits):
        circuit.h(i)  # Apply Hadamard gate
    for i in range(num_qubits - 1):
        circuit.cx(i, i + 1)  # Apply CNOT gate
    circuit.measure_all()
    return circuit

# Implement the Quantum Fourier Transform (QFT)

def qft_circuit(num_qubits: int):
    circuit = QuantumCircuit(num_qubits)
    for i in range(num_qubits):
        circuit.h(i)
        for j in range(i + 1, num_qubits):
            circuit.cp(np.pi / 2**(j - i), j, i)
    circuit.measure_all()
    return circuit
