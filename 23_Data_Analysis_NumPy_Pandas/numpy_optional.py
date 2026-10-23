# Python Basics to Advanced Example
# Run: python numpy_optional.py

try:
    import numpy as np
    values = np.array([1, 2, 3, 4])
    print("Mean:", values.mean(), "Squared:", values**2)
except ImportError:
    print("Install optional dependency with: python -m pip install numpy")
