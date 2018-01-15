class Class1:
    def __init__(self):
        print("Конструктор базового класса")
    def func1(self):
        print("Метод func1 класса Class1")

class Class2(Class1):
    def __init__(self):
        print("Конструктор производного класса")
        Class1.__init__(self)
    def func1(self):
        print("Метод func1 класса Class2")
        Class1.func1(self)
c = Class2()
c.func1()