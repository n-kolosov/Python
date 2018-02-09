try:
    x = 1/0
except (NameError, IndexError, ZeroDivisionError):
    print("Попытка деления на ноль")
    x = 0
print(x)