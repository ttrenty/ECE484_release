from qiskit import QuantumCircuit

import src.Q6b_BernsteinVazirani as Q6b

from tests_utils import require_impl, load_student_info, rng_from_seed

# ---------- Q6b: BV ----------


def build_bv_oracle(a: str) -> QuantumCircuit:
    """
    Public simple construction:
      n input qubits x, 1 target y;
      for each bit a_i=1, apply CNOT(x_i -> y).
    """
    n = len(a)
    qc = QuantumCircuit(n + 1)
    for i, bit in enumerate(
        reversed(a)
    ):  # reversed to match Qiskit little-endian if needed
        if bit == "1":
            qc.cx(i, n)  # from x_i to target
    return qc


def test_bernstein_vazirani_one_query():
    info = load_student_info()
    rng = rng_from_seed(info.seed)
    n = int(rng.integers(4, 9))
    a = "".join("1" if b else "0" for b in rng.integers(0, 2, size=n))
    oracle = build_bv_oracle(a)
    recovered = require_impl(Q6b.bernstein_vazirani, oracle)
    # Allow either MSB..LSB or LSB..MSB; normalize by reversing if necessary
    ok = (recovered == a) or (recovered[::-1] == a)
    assert ok, f"Recovered {recovered}, expected {a} (or reversed)"
