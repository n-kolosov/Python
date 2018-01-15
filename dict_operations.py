d = {1: "int", "a": 3, (1, 2): "val"}
print(d[1], d["a"], d[(1, 2)])

d = {"a": 2, "b": 6}
print("a" in d, "c" in d)
print("a" not in d, "c" not in d)
print(d.get("a"), d.get("c"), d.get("c", 800))
print(d.setdefault("a"), d.setdefault("c"), d.setdefault("d", 500))
d = {"a": 2, "b": 6}
d["b"] = 20
d["c"] = "String"
print(d)
print(len(d))
del d["b"]
print(d)