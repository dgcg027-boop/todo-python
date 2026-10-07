import requests

response = requests.get("https://jsonplaceholder.typicode.com/posts/1")

print(response.status_code)

data = response.json()
print(data["title"])
print(data["userId"])
print(len(data["body"]))

response = requests.get("https://jsonplaceholder.typicode.com/posts")
posts = response.json()
print(f"Всего постов : {len(posts)}")

for post in posts[:3]:
    print(f"- {post['title']}")