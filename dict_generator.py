keys = ["a", "b"]
values = [1, 2]
d = {k: v for (k, v) in zip(keys, values)}
print(d)
d = {"a": 1, "b": 2, "c": 3, "d": 4}
d = {k: v for (k, v) in d.items() if v % 2 == 0}
print(d)