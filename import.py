import time, math
print(time.strftime("%d.%m.%Y"))
print(math.pi)
print(getattr(math, "pi")) #возвращает значение константы pi из модуля math
#в math нет константы с именем x, поэтому вместо неё будет выведено предупреждение
print(getattr(math, "x", "There is no constant named x"))