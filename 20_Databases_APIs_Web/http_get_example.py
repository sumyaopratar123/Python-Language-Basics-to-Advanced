# Python Basics to Advanced Example
# Run: python http_get_example.py

from urllib.request import urlopen
from urllib.error import URLError

url = "https://example.com"
try:
    with urlopen(url, timeout=5) as response:
        print("Status:", response.status)
        print(response.read(200).decode("utf-8", errors="replace"))
except URLError as exc:
    print("Network request failed:", exc)
