words = {
    "кот": "cat",
    "собака": "dog",
    "дом": "house",
    "вода": "water"
}
word = input("Напиши слово для перевода: ").lower()
if word in words:
    print(f"{word} - {words[word]}")
else:
    print("Такого слова нет")