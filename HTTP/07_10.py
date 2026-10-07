import requests

response = requests.get("https://jsonplaceholder.typicode.com/posts/1")

print(response.status_code)     # 200
print(response.json())           # {'userId': 1, 'id': 1, 'title': '...', 'body': '...'}
