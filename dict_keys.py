d1, d2 = {"a": 1, "b": 2}, {"a":3, "c": 4, "d": 5}
print(d1.keys(), d2.keys())
print(list(d1.keys()), list(d2.keys()))

for k in d1.keys(): print(k, end=" ")
print()

for k in d2.keys(): print(k, end=" ")
print()

print(d1.keys() | d2.keys())
print(d1.keys() - d2.keys())
print(d1.keys() & d2.keys())
print(d1.keys() ^ d2.keys())