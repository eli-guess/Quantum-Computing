# Elijah Guess
# Quantum Circuit Simulation
# 1-22-2025

from qiskit import QuantumCircuit

# Implement Quantum Teleportation

def quantum_teleportation():

    circuit = QuantumCircuit(3, 3)

    # Create an entangled pair between qubits 1 and 2
    circuit.h(1)
    circuit.cx(1, 2)

    # Alice prepares a state to send (qubit 0)
    circuit.x(0)  # Example state |1⟩

    # Alice applies CNOT and Hadamard
    circuit.cx(0, 1)
    circuit.h(0)

    # Alice measures her qubits
    circuit.measure(0, 0)
    circuit.measure(1, 1)

    # Bob applies corrections
    circuit.cx(1, 2)
    circuit.cz(0, 2)

    # Bob measures his qubit to verify teleportation
    circuit.measure(2, 2)
    return circuit
