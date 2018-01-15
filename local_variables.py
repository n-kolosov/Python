def func():
    local1 = 77
    global1 = 25
    print("Значение global1 внутри функции=", global1)
global1 = 10
func()
print("Значение global1 вне функции=", global1)
try:
    print(local1)
except NameError:
    print("Переменная local1 не видна вне функции")