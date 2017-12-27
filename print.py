import sys as s

print("Строка 1")
print("Строка 2")

print("Строка 1", "Строка 2")

print ("Строка 1", "Строка 2", sep="")
print ("Строка 1", "Строка 2", sep="$")

print("Строка 1", "Строка 2", end=" ")
print("Строка 3")

print("Строка 1", "Строка 2", sep="12345", end="qwerty")
print("Строка 3")

for n in range (1, 5):
    print(n, end=" ")
print()
print("Этот текст на новой строке")

for n in range (1, 5):
    print(n)
print("Этот текст на новой строке")


for n in range (1, 5):
    print(n, end=" ")
print("Этот текст не на новой строке")

print('''Строка 1
Строка 2
Строка 3''')

s.stdout.write("Строка\n")
s.stdout.write("Строка1")
s.stdout.write("Строка2\n")
s.stdout.write("Строка1\n")
s.stdout.write("Строка2")