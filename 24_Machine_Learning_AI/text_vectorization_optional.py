# Python Basics to Advanced Example
# Run: python text_vectorization_optional.py

try:
    from sklearn.feature_extraction.text import CountVectorizer
    docs = ["python is fun", "python is useful", "data is useful"]
    vectorizer = CountVectorizer()
    print(vectorizer.fit_transform(docs).toarray())
    print(vectorizer.get_feature_names_out().tolist())
except ImportError:
    print("Install dependency: python -m pip install scikit-learn")
