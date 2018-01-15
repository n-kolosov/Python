d = dict(a = 1, b = 2)
print(d)
d = dict()
print(d)
d = dict({"a": 3, "b": 4})
print(d)
d = dict([("a", 5), ("b", 6)])
print(d)
d = dict([["a", 7], ["b", 8]])
print(d)

d = {"a": 1, "b": 5}
print(d)

d = {}
d["a"] = 3
d["b"] = 6
print(d)

d1 = {"a": 2, "b": 6}
d2 = dict(d1)
print(d1 is d2)
d2["b"] = 7
print(d1, d2)

d1 = {"a": 3, "b": 4}
d2 = d1.copy()
print(d1 is d2)