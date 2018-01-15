from abc import ABCMeta, abstractmethod
class Class1(metaclass=ABCMeta):
    @abstractmethod
    def func(self, x):
        pass

class Class2(Class1):
    def func(self, x):
        print(x)

class Class3(Class1):
    pass

c2 = Class2()
c2.func(50)
try:
    c3 = Class3()
    c3.func(50)
except TypeError as msg:
    print(msg)