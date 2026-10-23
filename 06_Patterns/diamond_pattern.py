# Python Basics to Advanced Example
# Run: python diamond_pattern.py

n = int(input("Half-height: "))
for i in range(1, n+1): print(" "*(n-i) + "*"*(2*i-1))
for i in range(n-1, 0, -1): print(" "*(n-i) + "*"*(2*i-1))
