try:
    try:
        x = 1/0
    except NameError:
        print("Неопределённый идентификатор")
    except IndexError:
        print("Неопределённый индекс")
    print("Выражение после вложенного обработчика")
except ZeroDivisionError:
    print("Попытка деления на ноль")
    x = 0
print(x)