#Controlando dados inseridos pelo input

try: 
    a = input("Type a number: ")
    b = input("Type a another number: ")
    a = int(a)
    b = int(b)
    print(a / b)
except (ZeroDivisionError, 
        ValueError):
    print("Invalid input.")