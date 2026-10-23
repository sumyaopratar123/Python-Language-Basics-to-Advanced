# Python Basics to Advanced Example
# Run: python file_search_tool.py

from pathlib import Path

root = Path(input("Folder to search (default .): ").strip() or ".")
term = input("Filename contains: ").casefold()
if not root.is_dir(): print("Folder does not exist")
else:
    matches = [str(p) for p in root.rglob("*") if p.is_file() and term in p.name.casefold()]
    print("\n".join(matches) if matches else "No matches")
