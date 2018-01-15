x = 5
func = lambda: x
x = 80
print(func())

x = 5
func = (lambda y: lambda: y)(x)
x = 80
print(func())

x = 5
func = lambda x=x: x
x = 80
print(func())