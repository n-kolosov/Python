import math
def hasattr_math(attr):
    if hasattr(math, attr):
        return "Атрибут существует"
    else:
        return "Атрибут не существует"
print(hasattr_math("pi"))
print(hasattr_math("e"))
print(hasattr_math("x"))