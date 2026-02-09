import random

secret_number = random.randint(1, 100)
attempts = 0

print("Угадай число от 1 до 100")

while True:
    guess = int(input("Введи число: "))
    attempts += 1
    
    if guess == secret_number:
        print(f"Правильно! Ты угадал/а за {attempts} попыток")
        break
    elif guess < secret_number:
        print("Число больше")
    else:
        print("Число меньше")
