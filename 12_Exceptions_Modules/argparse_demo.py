# Python Basics to Advanced Example
# Run: python argparse_demo.py

import argparse

parser = argparse.ArgumentParser(description="Demo command-line argument")
parser.add_argument("--name", default="Python")
args = parser.parse_args()
print(f"Hello, {args.name}!")
