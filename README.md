# Quantum Circuit Simulator

This project is an interactive quantum computing simulator built using Qiskit and Streamlit. It allows users to explore and simulate fundamental quantum circuits and algorithms while visualizing their results dynamically. The app includes detailed descriptions, mathematical foundations, and graphical outputs for each quantum circuit.

- - -

**Features**

Basic Quantum Circuit:

 - Demonstrates simple operations like the Hadamard and Pauli-X gates, illustrating quantum superposition and bit flipping.
 - Includes mathematical explanations with LaTeX-rendered equations.

Quantum Teleportation:

 - Simulates the quantum teleportation process to transfer quantum states using entanglement and classical communication.
 - Provides step-by-step equations and a detailed description.

Quantum Fourier Transform (QFT):

 - Implements the QFT to demonstrate quantum equivalents of the discrete Fourier transform.
 - Includes the mathematical basis and state transformations.

- - -

**Visualizations** 

 - The app renders quantum circuits using Qiskit's mpl backend for clear, tabbed circuit diagrams.
 - Simulation results are displayed as histograms, showing qubit measurement probabilities.

- - - 

**Technologies Used**

 - Qiskit: Quantum computing library for creating and simulating quantum circuits.
 - Streamlit: Framework for interactive and user-friendly web applications.
 - Matplotlib: For rendering quantum circuit diagrams and result histograms.

- - - 

**Installation** 

To get started, you need Python (preferably Python 3.10) and the necessary dependencies.

Clone the repository:

```
git clone https://github.com/eli-guess/Quantum-Computing.git
```

Install the required packages:

```
qiskit
streamlit
matplotlib
qiskit-aer
```

Run the Streamlit app:

```
streamlit run quantum_app.py
```

Purpose:

This project aims to provide an educational and interactive way to learn quantum computing concepts. It is suitable for students, enthusiasts, and professionals who want to deepen their understanding of quantum algorithms and explore the behavior of quantum systems through simulation.

License:

This project is licensed under the MIT License - see the LICENSE file for details.
