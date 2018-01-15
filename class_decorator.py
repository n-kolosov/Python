def deco(C):
    print("Внутри декоратора")
    return C

@deco
class MyClass:
    def __init__(self, value):
        self.v = value
c = MyClass(5)
print(c.v)