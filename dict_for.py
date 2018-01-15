d = {"x": 1, "y": 2, "z": 3}

for key in d.keys():
    print("({0} => {1})".format(key, d[key]), end=" ")

print()

for key in d:
    print("({0} => {1})".format(key, d[key]), end=" ")

print()

k = list(d.keys())
k.sort()
for key in k:
    print("({0} => {1})".format(key, d[key]), end=" ")

print()

for key in sorted(d.keys()):
    print("({0} => {1})".format(key, d[key]), end=" ")

print()

for key in sorted(d):
    print("({0} => {1})".format(key, d[key]), end=" ")