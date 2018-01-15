def deco(f):
    print("Вызвана функция func()")
    return f

@deco
def func(x):
    return "x = {0}".format(x)

print(func(10))
print(deco(func)(10))

def deco1(f):
    print("Вызвана функция deco1()")
    return f
def deco2(f):
    print("Вызвана функция deco2()")
    return f
@deco1
@deco2
def func(x):
    return "x = {0}".format(x)
print(func(10))