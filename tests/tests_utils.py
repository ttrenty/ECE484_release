"""
Lightweight utilities shared by tests
"""

from dataclasses import dataclass
import pytest
from pathlib import Path
from typing import Tuple

import numpy as np

try:
    # Qiskit imports grouped to keep import-time small
    from qiskit import QuantumCircuit
    from qiskit.quantum_info import Statevector, Operator
    from qiskit_aer import AerSimulator
except Exception:
    QuantumCircuit = object  # type: ignore
    Statevector = object  # type: ignore
    Operator = object  # type: ignore
    AerSimulator = object  # type: ignore


# -------------------- Student info & seeding --------------------


@dataclass
class StudentInfo:
    student_number: int
    seed: int
    variant_synthesis: str  # "A" or "B"


def load_student_info(path: str | Path = "student_info.yaml") -> StudentInfo:
    import yaml  # pinned in env

    with open(path, "r", encoding="utf-8") as f:
        d = yaml.safe_load(f)
    with open("random_seed.yaml", "r", encoding="utf-8") as f:
        d2 = yaml.safe_load(f)
    variant = "A" if int(d["student_number"]) % 2 == 0 else "B"
    return StudentInfo(
        student_number=int(d["student_number"]),
        seed=int(d2["seed"]),
        variant_synthesis=variant,
    )


def rng_from_seed(seed: int) -> np.random.Generator:
    return np.random.default_rng(int(seed) & 0xFFFFFFFF)


def require_impl(fn, *args, **kwargs):
    try:
        return fn(*args, **kwargs)
    except NotImplementedError as e:
        pytest.skip(str(e))


# -------------------- Linear algebra helpers --------------------


def normalize(psi: np.ndarray) -> np.ndarray:
    psi = np.asarray(psi, dtype=complex).reshape(-1)
    nrm = np.linalg.norm(psi)
    if nrm == 0:
        return psi
    return psi / nrm


def global_phase_align(a: np.ndarray, b: np.ndarray) -> Tuple[np.ndarray, np.ndarray]:
    """Return (a', b) where a' is rephased to align to b by overall phase."""
    a = np.asarray(a, dtype=complex).reshape(-1)
    b = np.asarray(b, dtype=complex).reshape(-1)
    phase = np.vdot(b, a)
    if phase == 0:
        return a, b
    return a * np.exp(-1j * np.angle(phase)), b


def fidelity(psi: np.ndarray, phi: np.ndarray) -> float:
    """|<psi | phi>|^2 with normalization and global-phase invariance."""
    psi = normalize(psi)
    phi = normalize(phi)
    psi, phi = global_phase_align(psi, phi)
    return float(np.abs(np.vdot(psi, phi)) ** 2)
