# Python Basics to Advanced Example
# Run: python plot_optional.py

try:
    import matplotlib.pyplot as plt
    months = ["Jan", "Feb", "Mar"]
    sales = [10, 14, 12]
    plt.plot(months, sales, marker="o")
    plt.title("Example Monthly Sales")
    plt.xlabel("Month"); plt.ylabel("Sales")
    plt.tight_layout(); plt.show()
except ImportError:
    print("Install optional dependency with: python -m pip install matplotlib")
