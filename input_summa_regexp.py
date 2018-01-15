import re
print("Ведите слово 'stop' для получения результата")
s = 0
p = re.compile(r"^[-]?[0-9]+$", re.S)
while True:
    x = input("Введите число: ")
    if x == "stop":
        break
    if not p.search(x):
        print("Необходимо ввести число, а не строку!")
        continue
    x = int(x)
    s += x
print("Сумма чисел равна:", s)