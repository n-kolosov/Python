print("""Укажите Вашу операционную систему
    1 - Windows 7
    2 - Windows 8
    3 - Ubuntu Linux
    4 - Mac OS
    5 - Другая""")
os = input("Введите число, соответствующее ответу: ")
if os != "":
    if os == "1":
        print("Вы выбрали Windows 7")
    elif os == "2":
        print("Вы выбрали Windows 8")
    elif os == "3":
        print("Вы выбрали Ubuntu Linux")
    elif os == "4":
        print("Вы выбрали Mac OS")
    elif os == "5":
        print("Вы выбрали другую ОС")
    else:
        print("Мы не можем определить вашу ОС")
else:
    print("Вы не ввели число")