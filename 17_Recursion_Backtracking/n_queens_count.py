# Python Basics to Advanced Example
# Run: python n_queens_count.py

def count_n_queens(n):
    cols, diag1, diag2 = set(), set(), set()
    def place(row):
        if row == n: return 1
        total = 0
        for col in range(n):
            if col in cols or row-col in diag1 or row+col in diag2: continue
            cols.add(col); diag1.add(row-col); diag2.add(row+col)
            total += place(row+1)
            cols.remove(col); diag1.remove(row-col); diag2.remove(row+col)
        return total
    return place(0)

print(count_n_queens(8))
