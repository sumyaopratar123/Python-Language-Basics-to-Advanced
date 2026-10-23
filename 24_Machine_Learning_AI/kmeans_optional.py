# Python Basics to Advanced Example
# Run: python kmeans_optional.py

try:
    from sklearn.cluster import KMeans
    X = [[1, 2], [1, 3], [10, 10], [11, 10]]
    model = KMeans(n_clusters=2, random_state=42, n_init=10).fit(X)
    print("Labels:", model.labels_.tolist())
except ImportError:
    print("Install dependency: python -m pip install scikit-learn")
