# Python Basics to Advanced Example
# Run: python student_marks_manager.py

students = {}
while True:
    name = input("Student name (or q): ").strip()
    if name.lower() == "q": break
    try:
        marks = float(input("Marks out of 100: "))
        if not 0 <= marks <= 100: raise ValueError
        students[name] = marks
    except ValueError: print("Enter marks between 0 and 100.")
if students:
    for name, marks in sorted(students.items()): print(name, marks)
    print("Class average:", sum(students.values())/len(students))
