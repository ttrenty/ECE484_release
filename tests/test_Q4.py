import numpy as np

import src.Q4_frameworks as Q4

from tests_utils import require_impl, load_student_info, rng_from_seed, fidelity


def _expected_statevector(theta: float, phi: float) -> np.ndarray:
    """
    Do not cheat and return this directly in your implementation! For Numpy you have to do the gate operations.
    """
    c0 = np.cos(theta / 2)
    s0 = np.sin(theta / 2)
    return np.array([c0, 0, 0, s0 * np.exp(1j * phi)], dtype=complex)


def test_shapes_and_types_qiskit():
    theta, phi = 0.7, 1.1
    sv_q = require_impl(Q4.build_target_state_qiskit, theta, phi)
    assert isinstance(sv_q, np.ndarray) and sv_q.shape == (4,)
    assert np.iscomplexobj(sv_q)


def test_qiskit_correctness():
    info = load_student_info()
    rng = rng_from_seed(info.seed)
    theta = rng.uniform(0, np.pi)
    phi = rng.uniform(0, 2 * np.pi)

    sv_q = require_impl(Q4.build_target_state_qiskit, theta, phi)
    F = fidelity(sv_q, _expected_statevector(theta, phi))
    assert F >= 0.999


def test_shapes_and_types_pennylane():
    theta, phi = 0.7, 1.1
    sv_p = require_impl(Q4.build_target_state_pennylane, theta, phi)
    assert isinstance(sv_p, np.ndarray) and sv_p.shape == (4,)
    assert np.iscomplexobj(sv_p)


def test_pennylane_correctness():
    info = load_student_info()
    rng = rng_from_seed(info.seed)
    theta = rng.uniform(0, np.pi)
    phi = rng.uniform(0, 2 * np.pi)

    sv_p = require_impl(Q4.build_target_state_pennylane, theta, phi)
    F = fidelity(sv_p, _expected_statevector(theta, phi))
    assert F >= 0.999


def test_numpy_bonus_shapes_and_types():
    theta, phi = 0.7, 1.1
    sv_n = require_impl(Q4.build_target_state_numpy, theta, phi)
    assert isinstance(sv_n, np.ndarray) and sv_n.shape == (4,)
    assert np.iscomplexobj(sv_n)


def test_numpy_bonus_correctness():
    # If students implement the bonus, it should match too.
    info = load_student_info()
    rng = rng_from_seed(info.seed)
    theta = rng.uniform(0, np.pi)
    phi = rng.uniform(0, 2 * np.pi)
    sv_n = require_impl(Q4.build_target_state_numpy, theta, phi)
    F = fidelity(sv_n, _expected_statevector(theta, phi))
    assert F >= 0.999
