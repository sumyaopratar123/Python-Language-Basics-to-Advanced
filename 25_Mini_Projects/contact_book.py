# Python Basics to Advanced Example
# Run: python contact_book.py

contacts = {}
while True:
    command = input("add/search/list/quit: ").strip().lower()
    if command == "add":
        name = input("Name: ").strip(); phone = input("Phone: ").strip()
        if name and phone: contacts[name] = phone
    elif command == "search": print(contacts.get(input("Name: ").strip(), "Not found"))
    elif command == "list":
        for name, phone in sorted(contacts.items()): print(name, phone)
    elif command == "quit": break
    else: print("Unknown command")
