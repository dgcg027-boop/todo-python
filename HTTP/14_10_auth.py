import requests
import json

response = requests.get(
    "https://httpbin.org/bearer",
    headers = {"Authorization": "Bearer my_token_123"}
    )
print(response.status_code)
print(response.json())

session = requests.Session()
session.headers.update({"Authorization": "Bearer test123"})
session.get("https://httpbin.org/bearer")
session.get("https://httpbin.org/headers")
print(response.json())

response = requests.get("https://httpbin.org/html")
print(response.ok)
print(response.text[:100])