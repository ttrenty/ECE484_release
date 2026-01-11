"""
Example: Using a Noisy Simulator with FakeManilaV2 Backend

This example demonstrates how to simulate quantum circuits with realistic noise
using Qiskit's fake backend for the IBM Manila device.

The FakeManilaV2 backend provides a noise model based on the calibration data
from a real IBM quantum computer, allowing you to test how your circuits would
perform on actual hardware.
"""

from qiskit import QuantumCircuit, transpile
from qiskit_aer import AerSimulator
from qiskit_ibm_runtime.fake_provider import FakeManilaV2


def noiseless_simulation_example():
    """
    Create and run a simple quantum circuit on a noiseless simulator. Read the second qubit.
    """
    # Create a noiseless Aer simulator
    simulator = AerSimulator()

    # Example: Create a Bell state circuit
    qc = QuantumCircuit(2)
    qc.h(0)
    qc.cx(0, 1)

    qc.save_probabilities([1], label="qubit_1_probs")  # Save probabilities of qubit 1

    sim = AerSimulator(method="statevector")
    # Run a single shot since we are using noiseless simulation
    result = sim.run(qc, shots=1).result()
    probs = result.data(0)["qubit_1_probs"]  # length-2 list: [P(0), P(1)]

    print("Noiseless simulation results for qubit 1:")
    print(f"P(0) = {probs[0]:.4f}, P(1) = {probs[1]:.4f}")
    print()  # Blank line for readability


def noisy_simulation_example():
    """
    Create and run a simple quantum circuit on a noisy simulator
    based on the FakeManilaV2 backend.
    """
    # Create a fake backend representing the IBM Manila device
    backend = FakeManilaV2()

    # Create a noisy simulator from the backend
    # This simulator will include realistic gate errors, readout errors, etc.
    noisy_sim = AerSimulator.from_backend(backend)

    # Example: Create a Bell state circuit
    qc = QuantumCircuit(2)
    qc.h(0)
    qc.cx(0, 1)
    qc.measure_all()

    # Transpile the circuit for the noisy simulator
    # This optimizes the circuit for the backend's gate set and connectivity
    tqc = transpile(qc, noisy_sim)

    # Run the circuit on the noisy simulator, running it multiple times to average out noise
    result = noisy_sim.run(tqc, shots=8192).result()
    counts = result.get_counts()

    print("Measurement results with noise:")
    print(counts)
    print()
    print("Note: In an ideal Bell state, we would only see '00' and '11'.")
    print("With noise, you may also see '01' and '10' due to errors.")


if __name__ == "__main__":
    noiseless_simulation_example()
    noisy_simulation_example()
