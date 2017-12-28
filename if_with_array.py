print("""Укажите Вашу операционную систему
    1 - Windows 7
    2 - Windows 8
    3 - Ubuntu Linux
    4 - Mac OS
    5 - Другая""")
os = int(input("Введите число, соответствующее ответу: "))
arr = ['Вы выбрали Windows 7', 'Вы выбрали Windows 8', 'Вы выбрали Ubuntu Linux', 'Вы выбрали Mac OS', 'Вы выбрали другую ОС']
try:
    print(arr[os+1])
except Exception:
    print("Не можем определить Вашу ОС")