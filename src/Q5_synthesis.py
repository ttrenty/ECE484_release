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

    If your student number is even, implement Variant A, use only gates RY and RZ.
    If your student number is odd, implement Variant B, use only the U gate.

    Return:
        QuantumCircuit with 1 qubit and 0 classical bits (no measurements).
    """
    # TODO: Implement per your assigned variant (A or B).
    raise NotImplementedError("prepare_single not implemented")


def prepare_bell(kind: str) -> QuantumCircuit:
    """
    kind in {"phi+", "phi-", "psi+", "psi-"}.
    Implement `prepare_bell(kind) -> QuantumCircuit` to prepare Bell states from $|00\rangle$ using only $H$ and $CX$:
    Returns a 2-qubit circuit (no measurements) that prepares the requested Bell state from |00>.
    """
    # TODO: Implement this function
    k = kind.strip().lower()
    raise NotImplementedError("prepare_bell not implemented")


def unitary_equal(
    circA: QuantumCircuit, circB: QuantumCircuit, tol: float = 1e-10
) -> bool:
    """
    Compare unitaries modulo global phase.
    """
    # TODO: Implement this function, find the one method to use in qiskit.quantum_info.Operator.
    raise NotImplementedError("unitary_equal not implemented")
