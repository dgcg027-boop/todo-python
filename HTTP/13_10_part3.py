import requests

try:
    response = requests.get("https://jsonplaceholder.typicode.com/posts/1", timeout=5)
    response.raise_for_status()
    data = response.json()
    print(data["title"])
except requests.exceptions.ConnectionError:
    print("Нет соединения с сервером")
except requests.exceptions.Timeout:
    print("Сервер не ответил вовремя")
except requests.exceptions.HTTPError as e:
    print(f"ошибка HTTP: {e}")

response1 = requests.get("https://jsonplaceholder.typicode.com/posts/9999")
if response1.status_code == 200:
    data = response1.json()
    print(data["title"])
elif response1.status_code == 404:
    print("Не найдено")
else:
    print(f"Ошибка: {response1.status_code}")

response2 = requests.get("https://jsonplaceholder.typicode.com/posts/1")

print(response2.headers)
print(response2.headers["Content-Type"])