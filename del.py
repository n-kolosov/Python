class MyClass:
    def __init__(self):
        print("Вызван метод __init__()")
    def __del__(self):
        print("Вызван метод __del__()")
c1 = MyClass()
del c1
c2 = MyClass()
c3 = c2
del c2
del c3