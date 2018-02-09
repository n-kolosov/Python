try:
    x = 1/0
except ZeroDivisionError:
    print("Деление на ноль")
    x = 0
print(x)