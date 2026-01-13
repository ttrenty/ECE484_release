"""
Q5 (Synthesis): Qiskit-only.
- Prepare a 1-qubit target |psi(theta, phi)> from |0>.
- Prepare Bell states.
- Implement a robust unitary_equal (global-phase insensitive).
"""

from qiskit import QuantumCircuit
from qiskit.quantum_info import Operator


def prepare_single(theta: float, phi: float) -> QuantumCircuit:
    """
    Prepare |psi(theta, phi)> = cos(theta/2)|0> + e^{i phi} sin(theta/2)|1> from |0>.

    Implement using the generic U gate.

    Return:
        QuantumCircuit with 1 qubit and 0 classical bits (no measurements).
    """
    # TODO: Implement.
    raise NotImplementedError("prepare_single not implemented")


def prepare_bell(subscript: str) -> QuantumCircuit:
    """
    subscript in {"00", "10", "01", "11"}, corresponding to Bell states {"phi+", "phi-", "psi+", "psi-"} respectively.
    
    Implement `prepare_bell(subscript) -> QuantumCircuit` to prepare Bell states from $|00\rangle$ using only $H$ and $CX$:
    
    Return:
        QuantumCircuit with 2 qubits and 0 classical bits (no measurements) that prepares the requested Bell state from |00>.
    """
    # TODO: Implement this function
    raise NotImplementedError("prepare_bell not implemented")


def unitary_equal(
    circA: QuantumCircuit, circB: QuantumCircuit, tol: float = 1e-10
) -> bool:
    """
    Compare unitaries modulo global phase.
    """
    # TODO: Implement this function, using qiskit.quantum_info.Operator and one of its methods.
    raise NotImplementedError("unitary_equal not implemented")
