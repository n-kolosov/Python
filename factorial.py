def factorial(n):
    if n == 0 or n == 1: return 1
    else:
        return n * factorial(n - 1)

x = int(input("Введите число: "))
print("Факториал числа {0} = {1}".format(x, factorial(x)))