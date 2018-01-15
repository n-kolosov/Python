class MyClass:
    def __setattr__(self, attr, value):
        print("Вызван метод __setattr__()")
        self.__dict__[attr] = value #Только так
c = MyClass()
c.i = 10
print(c.i)