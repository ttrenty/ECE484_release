"""
Q6b (Bernstein-Vazirani): Qiskit-only BV algorithm for hidden bit-string recovery.
"""

from qiskit import QuantumCircuit, transpile
from qiskit_aer import AerSimulator


def bernstein_vazirani(oracle: QuantumCircuit) -> str:
    """
    Recover secret string a in one query using the given oracle circuit.

    The oracle given in argument implements f_a(x) = a · x (mod 2) in the usual BV style.

    Return the recovered bit-string a
    """
    # TODO: Implement the Bernstein-Vazirani algorithm
    # Hint:
    # 1. Compute n as oracle.num_qubits-1 (where the oracle has n input qubits + 1 qubit used as target to store f_a(x)). The n first qubits are the input register.
    # 2. Create circuit with n+1 qubits and n classical bits
    # 3. Initialize target qubit (last one) to |1> using X gate
    # 4. Apply Hadamard to all qubits
    # 5. Compose the oracle circuit
    # 6. Apply Hadamard to input qubits only
    # 7. Measure all input qubits
    # 8. Run on AerSimulator and return the measured bitstring, meaning the state of the n classical bits after measurement (in the computational basis).
    raise NotImplementedError("bernstein_vazirani not implemented")
