# Python Basics to Advanced Example
# Run: python simple_http_server.py

from http.server import HTTPServer, SimpleHTTPRequestHandler

# Run locally, then visit http://127.0.0.1:8000
server = HTTPServer(("127.0.0.1", 8000), SimpleHTTPRequestHandler)
print("Serving on http://127.0.0.1:8000 (Ctrl+C to stop)")
try:
    server.serve_forever()
except KeyboardInterrupt:
    print("\nServer stopped.")
finally:
    server.server_close()
