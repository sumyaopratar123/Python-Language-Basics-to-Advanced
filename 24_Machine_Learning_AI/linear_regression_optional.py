# Python Basics to Advanced Example
# Run: python linear_regression_optional.py

try:
    import numpy as np
    from sklearn.linear_model import LinearRegression
    X = np.array([[1], [2], [3], [4]])
    y = np.array([3, 5, 7, 9])
    model = LinearRegression().fit(X, y)
    print("Prediction for 5:", model.predict([[5]])[0])
except ImportError:
    print("Install dependencies: python -m pip install numpy scikit-learn")
