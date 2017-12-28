print("""Укажите Вашу операционную систему
    1 - Windows 7
    2 - Windows 8
    3 - Ubuntu Linux
    4 - Mac OS
    5 - Другая""")
os = int(input("Введите число, соответствующее ответу: "))
h = {1: 'Вы выбрали Windows 7', 2: 'Вы выбрали Windows 8', 3: 'Вы выбрали Ubuntu Linux', 4: 'Вы выбрали Mac OS', 5: 'Вы выбрали другую ОС'}
try:
    print(h[os])
except Exception:
    print("Не можем определить Вашу ОС")