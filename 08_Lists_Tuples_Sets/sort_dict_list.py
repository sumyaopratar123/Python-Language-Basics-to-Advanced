# Python Basics to Advanced Example
# Run: python sort_dict_list.py

students = [{"name":"Asha","marks":90}, {"name":"Ravi","marks":82}]
print(sorted(students, key=lambda s: s["marks"], reverse=True))
