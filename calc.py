ch1 = float(input("Первое число: "))

while True:
    op = input("Операция (+, -, *, /, %, //) или 'q' для выхода: ")
    
    if op == 'q':
        break
    
    ch2 = float(input("Второе число: "))
    
    if op == '+':
        result = ch1 + ch2
    elif op == '-':
        result = ch1 - ch2
    elif op == '*':
        result = ch1 * ch2
    elif op == '/':
        result = ch1 / ch2
    elif op == '%':
        result = ch1 % ch2
    elif op == '//':
        result = ch1 // ch2
    
    print(f"Результат: {result}")   
