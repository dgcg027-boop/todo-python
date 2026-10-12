import requests

response = requests.get("https://jsonplaceholder.typicode.com/posts/1")
print(response.status_code)

data = response.json()
print(data["title"])
print(data["userId"])
print(data["body"])

response = requests.get("https://jsonplaceholder.typicode.com/users")
users = response.json()

for user in users:
    print(f"{user['name']} - {user['email']}")