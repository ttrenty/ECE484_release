import numpy as np

from qiskit import QuantumCircuit
from qiskit.quantum_info import Statevector

import src.Q6a_SwapTest as Q6a

from tests_utils import require_impl, load_student_info, rng_from_seed, fidelity

# ---------- Helper to build psi/phi circuits from 1q statevectors ----------


def _circ_from_state_1q(theta, phi):
    qc = QuantumCircuit(1)
    qc.ry(theta, 0)
    qc.rz(phi, 0)
    return qc


# ---------- Q6a: SWAP test ----------


def test_swap_test_noiseless_matches_analytic():
    info = load_student_info()
    rng = rng_from_seed(info.seed)

    # Random 1q states via angles
    th1, ph1 = rng.uniform(0, np.pi), rng.uniform(0, 2 * np.pi)
    th2, ph2 = rng.uniform(0, np.pi), rng.uniform(0, 2 * np.pi)

    psi = _circ_from_state_1q(th1, ph1)
    phi = _circ_from_state_1q(th2, ph2)

    p0_emp = require_impl(Q6a.swap_test_noiseless, psi, phi)

    # Analytic overlap
    v1 = Statevector.from_instruction(psi).data
    v2 = Statevector.from_instruction(phi).data
    overlap = fidelity(v1, v2) ** 0.5  # |<psi|phi>|
    p0_th = (1 + overlap**2) / 2.0
    assert abs(p0_emp - p0_th) < 0.05  # generous tolerance for finite shots


def test_swap_test_noisy_matches_analytic():
    info = load_student_info()
    rng = rng_from_seed(info.seed)

    # Random 1q states via angles
    th1, ph1 = rng.uniform(0, np.pi), rng.uniform(0, 2 * np.pi)
    th2, ph2 = rng.uniform(0, np.pi), rng.uniform(0, 2 * np.pi)

    psi = _circ_from_state_1q(th1, ph1)
    phi = _circ_from_state_1q(th2, ph2)

    _ = require_impl(Q6a.swap_test_noisy, psi, phi, info.seed, shots=42)
    print("\nPrint statements from test_swap_test_matches_analytic:")
    for shots in [10, 100, 1000, 10000]:
        p0_emp = require_impl(Q6a.swap_test_noisy, psi, phi, info.seed, shots=shots)
        print(f"Shots: {shots:5d}, Measured p0: {p0_emp:8.4f}")

    p0_emp = require_impl(Q6a.swap_test_noisy, psi, phi, info.seed, shots=1000)

    # Analytic overlap
    v1 = Statevector.from_instruction(psi).data
    v2 = Statevector.from_instruction(phi).data
    overlap = fidelity(v1, v2) ** 0.5  # |<psi|phi>|
    p0_th = (1 + overlap**2) / 2.0
    assert abs(p0_emp - p0_th) < 0.05  # generous tolerance for finite shots
