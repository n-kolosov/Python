class MyClass:
    def __init__(self, value):
        self.__var = value
    def get_var(self):
        return self.__var
    def set_var(self, value):
        self.__var = value
    def del_var(self):
        del self.__var
    v = property(get_var, set_var, del_var, "Строка документирования")
c = MyClass(5)
c.v = 35
print(c.v)
del c.v

class MyClass:
    def __init__(self, value):
        self.__var = value
    @property
    def v(self):
        return self.__var
    @v.setter
    def v(self, value):
        self.__var = value
    @v.deleter
    def v(self):
        del self.__var
c = MyClass(5)
c.v = 35
print(c.v)
del c.v