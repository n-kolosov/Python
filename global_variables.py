def func(glob2):
    print("Значение глобальной переменной glob1 =", glob1)
    glob2 += 10
    print("Значение локальной переменной glob2=", glob2)

glob1, glob2 = 10, 5
func(77)
print("Значение глобальной переменной glob2=", glob2)