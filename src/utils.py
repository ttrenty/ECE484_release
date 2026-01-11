import numpy as np

# -------------------- Linear algebra helpers --------------------


def kron(*mats: np.ndarray) -> np.ndarray:
    out = np.array([[1]], dtype=complex)
    for m in mats:
        out = np.kron(out, m)
    return out
