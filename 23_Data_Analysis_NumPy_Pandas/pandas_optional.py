# Python Basics to Advanced Example
# Run: python pandas_optional.py

try:
    import pandas as pd
    df = pd.DataFrame({"name": ["Asha", "Ravi"], "marks": [90, 85]})
    print(df)
    print(df["marks"].mean())
except ImportError:
    print("Install optional dependency with: python -m pip install pandas")
