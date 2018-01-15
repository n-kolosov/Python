print("Ведите слово 'stop' для получения результата")
s = 0
while True:
    x = input("Введите число: ")
    if x == "stop":
        break
    x = int(x)
    s += x
print("Сумма чисел равна:", s)