"""
Q4 (Frameworks): Build the same 2-qubit target state in Qiskit and PennyLane.
Bonus: reproduce with pure NumPy matrices.

Return raw statevectors (shape (4,)), not circuits.
"""

import math
import numpy as np

# Qiskit
from qiskit import QuantumCircuit
from qiskit.quantum_info import Statevector

# PennyLane
import pennylane as qml

# For Numpy Bonus
from src.utils import kron


def build_target_state_qiskit(theta: float, phi: float) -> np.ndarray:
    """
    Prepare |Psi> = cos(theta/2)|00> + e^{i phi} sin(theta/2)|11>
    using a minimal {H, CX, RY, RZ}-style construction in Qiskit.

    Returns:
        np.ndarray: shape (4,), complex statevector in computational basis.
    """
    # TODO: Implement this function, remove the raise NotImplementedError line as well, do that for all future functions too.
    # Hint (lucky for you if you read this before doing Q2): One canonical construction you can use is:
    # - RY(theta) on qubit 0
    # - CX(0, 1) to entangle
    # - RZ(phi) on qubit 1
    # Create a QuantumCircuit with 2 qubits and apply gates on it using methods like ry(angle, qubit), cx(control, target), rz(angle, qubit). Then extract the statevector using Statevector.from_circuit()
    raise NotImplementedError("build_target_state_qiskit not implemented")


def build_target_state_pennylane(theta: float, phi: float) -> np.ndarray:
    """
    Same target state but using PennyLane (function-style circuit).
    Be careful of the shape of the returned statevector.
    """
    # TODO: Implement this function using PennyLane
    # Hint: Use qml.device("default.qubit", wires=2)
    # Create an inner @qml.qnode decorated function that applies gates (qml.RY, qml.CNOT, qml.RZ) and that returns qml.state(). Return its result as applied to theta and phi.
    raise NotImplementedError("build_target_state_pennylane not implemented")


# -------------------- Bonus (+3): NumPy only --------------------


def build_target_state_numpy(theta: float, phi: float) -> np.ndarray:
    """
    Returns the state but using your own NumPy matrix operations only.
    4x4 matrices for 2-qubit gates can be built via Kronecker products of two 2x2 gates (kron from utils.py).
    """
    # TODO (BONUS): Implement this function using only NumPy matrix operations
    # Define the necessary gate matrices: RY, RZ, CX, I2 (2x2 identity). Those can be helper functions.
    # Start with |00> = np.array([1, 0, 0, 0])
    # Hint: Use the helper functions `kron` from utils to create 4x4 matrices (2-qubits gates). Apply gates: kron(RY(theta), I2()); meaning RY on qubit 0, identity on qubit 1, followed by CX, followed by kron(I2(), RZ(phi))
    raise NotImplementedError("build_target_state_numpy (bonus) not implemented")
