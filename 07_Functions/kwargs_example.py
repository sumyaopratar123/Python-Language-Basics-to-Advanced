# Python Basics to Advanced Example
# Run: python kwargs_example.py

def show_details(**details):
    for key, value in details.items(): print(f"{key}: {value}")

show_details(name="Asha", role="student")
