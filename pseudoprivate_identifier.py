class MyClass:
    def __init__(self, x):
        self.__privateVar = x
    def set_var(self, x):
        self.__privateVar = x
    def get_var(self):
        return self.__privateVar
c = MyClass(10)
print(c.get_var())
c.set_var(20)
print(c.get_var())
try:
    print(c.__privateVar)
except AttributeError as msg:
    print(msg)

c._MyClass__privateVar = 50
print(c.get_var())