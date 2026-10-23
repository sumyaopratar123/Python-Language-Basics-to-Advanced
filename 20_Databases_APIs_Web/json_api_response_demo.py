# Python Basics to Advanced Example
# Run: python json_api_response_demo.py

import json

response = {"status": "ok", "data": {"message": "Hello API"}}
print(json.dumps(response, indent=2))
