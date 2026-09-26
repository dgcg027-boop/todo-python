name = input("Как тебя зовут?")
age = int(input("Сколько тебе лет?"))
if age < 0 or age > 120:
    print(f"{name}, ты вводишь что-то странное.")
elif age < 7:
    print(f"{name}, тебе в детский сад.")
elif age <= 17:
    print(f"{name}, тебе в школу.")
elif age <= 22:
    print(f"{name}, тебе в универ.")
elif age > 22:
    print(f"{name}, тебе работать.")