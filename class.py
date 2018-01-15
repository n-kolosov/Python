class MyClass:
    def __init__(self):
        self.x = 10 #атрибут экземпляра класса
    def print_x(self):
        print(self.x)
c = MyClass()

c.print_x()
print(c.x)
print(getattr(c, "x"))
print(getattr(c, "y", 0))
setattr(c, "y", 20)
print(getattr(c, "y", 0))
delattr(c, "y")
print(getattr(c, "y", 0))
print(hasattr(c, "x"))
print(hasattr(c, "y"))

class MyClass:
    pass
MyClass.x = 50
c1, c2 = MyClass(), MyClass()
c1.y = 10
c2.y = 20
print(c1.x, c1.y)
print(c2.x, c2.y)

class MyClass:
    x = 10 #атрибут объекта класса
    def __init__(self):
        self.y = 20 #атрибут экземпляра класса
c1, c2 = MyClass(), MyClass()
print(c1.x, c2.x)
MyClass.x = 40 #изменяем атрибут объекта класса
print(c1.x, c2.x)
c2.x = 42 #изменяем атрибут экземпляра класса
print(c1.x, c2.x)