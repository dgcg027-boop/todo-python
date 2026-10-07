import requests

response = requests.get("https://jsonplaceholder.typicode.com/users")
users = response.json()

for user in users:
    print(f"{user['name']} ({user['email']}) ({user['phone']}) - {user['address']['city']}\n")
