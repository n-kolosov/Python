class MyClass:
    def __init__(self):
        self.i = 20
    def __getattr__(self, attr):
        print("Аттрибут не существует")
        return 0
c = MyClass()
print(c.i)
print(c.s)