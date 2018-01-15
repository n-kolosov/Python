class Class1:
    def func(self, x):
        raise NotImplementedError("Необходимо переопределить метод")

class Class2(Class1):
    def func(self, x):
        print(x)

class Class3(Class1):
    pass

c2 = Class2()
c2.func(50)
c3 = Class3()
try:
    c3.func(50)
except NotImplementedError as msg:
    print(msg)