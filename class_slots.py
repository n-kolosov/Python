class MyClass:
    __slots__ = ["x", "y"]
    def __init__(self, a, b):
        self.x, self.y = a, b
c = MyClass(1, 2)
print(c.x, c.y)
c.x, c.y = 10, 20
print(c.x, c.y)
try:
    c.z = 50
except AttributeError as msg:
    print(msg)