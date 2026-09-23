import numpy as np

def cosine_similarity(a: list, b: list) -> float:
    """
    Returns the cosine similarity as a Python float.
    """
    # Write code here
    t = np.dot(a, b)
    d = np.linalg.norm(a) * np.linalg.norm(b)
    if d == 0: return 0.0
    return (float) (t / d)
    pass