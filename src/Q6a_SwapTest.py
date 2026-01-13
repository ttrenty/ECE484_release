"""
Q6a (SWAP Test): Qiskit-only SWAP test overlap estimator.
"""

from qiskit import QuantumCircuit, transpile
from qiskit_aer import AerSimulator

# If you want the Fake backend noise model:
from qiskit_ibm_runtime.fake_provider import FakeManilaV2


def swap_test_noiseless(psi: QuantumCircuit, phi: QuantumCircuit) -> float:
    """
    Build the standard SWAP-test circuit:
      ancilla |0> --H--●--H-- measure
                       |
                      SWAP(psi, phi)
    psi and phi are circuits that prepare their states from |0...0>.
    You must append them onto disjoint registers.

    Return empirical P(ancilla = 0).

    Noiseless SWAP test: return exact P(ancilla=0) without constructing the full statevector.
    Uses Aer 'save_probabilities' to get the ancilla marginal distribution.
    """
    # TODO: Implement the SWAP test circuit using AerSimulator's save_probabilities
    # Hint:
    # 1. Create a circuit with 1 ancilla + n qubits for psi + n qubits for phi, where you must extract the number of qubits n from the given QuantumCircuit objects psi and phi, they are not necessarily of the same size.
    # 2. Apply H to ancilla
    # 3. Compose psi and phi circuits onto their respective registers using the method .compose(...)
    # 4. Apply controlled-SWAP between corresponding qubits of psi and phi registers using qc.cswap(control, target1, target2)
    # 5. Apply H to ancilla
    # 6. Use qc.save_probabilities([ancilla_index], label="anc_probs") to save the marginal probabilities of the ancilla qubit
    # 7. Run on AerSimulator(method="statevector") and extract the probabilities from the result
    # See examples/aer_simulator_examples.py for a complete example of noisy simulation. Run it using `pixi run python examples/aer_simulator_examples.py`
    raise NotImplementedError("swap_test_noiseless not implemented")


def swap_test_noisy(
    psi: QuantumCircuit,
    phi: QuantumCircuit,
    random_seed,
    shots: int = 4096,
) -> float:
    """
    Noisy version of the SWAP test using a realistic noise model from FakeManilaV2.
    Return empirical P(ancilla = 0).
    """
    # TODO: Implement the SWAP test circuit using AerSimulator with noise from FakeManilaV2
    # Hint:
    # 1. Create a circuit as previously but allocate 1 classical bit for measuring the ancilla
    # 2. Apply the same steps as before to build the SWAP test circuit
    # 3. Measure the ancilla into the classical bit using the method qc.measure(ancilla_index, classical_bit_index)
    # 4. Create a noisy simulator using AerSimulator.from_backend(FakeManilaV2())
    # 5. Transpile the circuit for the noisy simulator using transpile(qc, noisy_sim, seed_transpiler=random_seed)
    # 6. Run the transpiled circuit on the noisy simulator with the given shots and random_seed for the simulator RNG, don't forget the seed_simulator=random_seed argument
    # 7. Extract the counts from the result and compute P(ancilla=0)
    # See examples/aer_simulator_examples.py for a complete example of noisy simulation.
    raise NotImplementedError("swap_test_noisy not implemented")
