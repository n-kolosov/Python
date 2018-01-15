def func(x, y):
    for i in range(1, x+1):
        yield i**y
for n in func(10, 2):
    print(n, end=" ")
print()
for n in func(10, 3):
    print(n, end=" ")
print()
for n in func(10, 4):
    print(n, end=" ")
print()
i = func(3, 3)
print(i.__next__())
print(i.__next__())
print(i.__next__())

def gen(l):
    for e in l:
        yield from range(1, e+1)

l = [5, 10]
for i in gen([5, 10]): print(i, end=" ")
print()
def gen2(n):
    for e in range(1, n+1):
        yield e*2

def gen(l):
    for e in l:
        yield from gen2(e)

l = [5, 10]
for i in gen([5, 10]): print(i, end=" ")