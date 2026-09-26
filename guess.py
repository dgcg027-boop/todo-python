secret = 42
attempts = 0
while True:
    число= int(input ("Напиши число"))
    attempts +=1
    if число < secret:
        print ("Больше")
    elif число > secret:
        print ("Меньше")
    else:
        print (f"Угадал! Попыток: {attempts}") 
        break