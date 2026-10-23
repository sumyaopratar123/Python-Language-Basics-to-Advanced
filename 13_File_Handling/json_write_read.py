# Python Basics to Advanced Example
# Run: python json_write_read.py

import json

data = {"name": "Asha", "skills": ["Python", "SQL"]}
serialized = json.dumps(data, indent=2)
print(serialized)
print(json.loads(serialized))
