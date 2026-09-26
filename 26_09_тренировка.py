text = input("Введите текст ")
count = 0
vowels = "аеёиоуыэюя"
for letter in text:
    if letter in vowels:
        count +=1

print(f"результат: {count}")