import numpy as np
import pytest

from qiskit.quantum_info import Statevector
from qiskit import QuantumCircuit

import src.Q5_synthesis as Q5

from tests_utils import require_impl, load_student_info, rng_from_seed, fidelity


def _target_1q(theta, phi):
    return np.array(
        [np.cos(theta / 2), np.exp(1j * phi) * np.sin(theta / 2)], dtype=complex
    )


def _statevector(qc):
    return Statevector.from_instruction(qc).data


def test_prepare_single_matches_target_and_template():
    info = load_student_info()
    rng = rng_from_seed(info.seed)

    theta = rng.uniform(0, np.pi)
    phi = rng.uniform(0, 2 * np.pi)

    qc = require_impl(Q5.prepare_single, theta, phi)
    assert isinstance(qc, QuantumCircuit)
    sv = _statevector(qc)
    F = fidelity(sv, _target_1q(theta, phi))
    assert F >= 0.999


def test_prepare_single_has_correct_gates_for_variant():
    info = load_student_info()
    rng = rng_from_seed(info.seed)
    theta = rng.uniform(0, np.pi)
    phi = rng.uniform(0, 2 * np.pi)
    qc = require_impl(Q5.prepare_single, theta, phi)

    # Light structure checks per variant (not exhaustive; stronger checks in hidden tests)
    ops = [inst.operation.name.lower() for inst in qc.data]
    if info.variant_synthesis == "A":
        assert "ry" in ops and "rz" in ops
    elif info.variant_synthesis == "B":
        # Qiskit 1.1+ has "u"
        assert any(g in ops for g in ("u"))
    else:
        pytest.fail(f"Unknown variant_synthesis: {info.variant_synthesis}")


def test_bell_states_format():
    for kind in ["phi+", "phi-", "psi+", "psi-"]:
        qc = require_impl(Q5.prepare_bell, kind)
        sv = _statevector(qc)
        # Quick projector expectations (relative comparisons)
        assert sv.shape == (4,)
        assert np.isclose(np.linalg.norm(sv), 1.0)


def phi_plus():
    return np.array([1, 0, 0, 1], dtype=complex) / np.sqrt(2)


def phi_minus():
    return np.array([1, 0, 0, -1], dtype=complex) / np.sqrt(2)


def psi_plus():
    return np.array([0, 1, 1, 0], dtype=complex) / np.sqrt(2)


def psi_minus():
    return np.array([0, 1, -1, 0], dtype=complex) / np.sqrt(2)


def test_bell_states_correctness():
    targets = {
        "phi+": phi_plus(),
        "phi-": phi_minus(),
        "psi+": psi_plus(),
        "psi-": psi_minus(),
    }
    for kind, target in targets.items():
        qc = require_impl(Q5.prepare_bell, kind)
        sv = _statevector(qc)
        F = fidelity(sv, target)
        assert F >= 0.999, f"Fidelity for {kind} was {F}"


def test_unitary_equal_basic():
    # HSH = e^{i pi/2} RX(pi/2)

    a = QuantumCircuit(1)
    a.h(0)
    a.s(0)
    a.h(0)  # H S H

    b = QuantumCircuit(1)
    b.rx(np.pi / 2, 0)

    assert require_impl(Q5.unitary_equal, a, b, tol=1e-9)
