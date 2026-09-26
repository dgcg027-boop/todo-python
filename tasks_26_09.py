def count_vowels(text):
    text = text.lower()
    count = 0
    for letter in text:
        if letter in "аеёиоуыэюя":
            count +=1

    return count

result = count_vowels("ААААА")
print(result)   # должно быть 3: и, е, и