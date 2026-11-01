import numpy as np

def flip(a: np.ndarray) -> np.ndarray:
    """Reverse 1-D array a without slicing a[::-1]."""
    index = np.array([i for i in reversed(range(len(a)))])
    return  a[index]