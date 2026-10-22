import requests

response = requests.get("https://jsonplaceholder.typicode.com/posts/1")
data = response.json()
print(data["title"])
print(data["userId"])

response1 = requests.get("https://jsonplaceholder.typicode.com/users/2")
data = response1.json()
print(data["name"])
print(data["email"])

response2 = requests.post(
    "https://jsonplaceholder.typicode.com/posts",
    json = {"title": "Тест", "body": "Привет", "userId": 3}
    )
print(response2.status_code)