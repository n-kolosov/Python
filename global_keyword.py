def func():
    global global1
    global1 = 25
    print("Значение global1 внутри функции =", global1)
global1 = 10
print("Значение global1 вне функции =", global1)
func()
print("Значение global1 после вызова функции=", global1)