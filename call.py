class MyClass:
    def __init__(self, m):
        self.msg = m
    def __call__(self):
        print(self.msg)

c1 = MyClass("Значение1")
c2 = MyClass("Значение2")
c1()
c2()