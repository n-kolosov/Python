h = {'x': 1, 'y': 2, 'z': 3}
for key in h.keys():
    print(key, h[key])
for key in h:
    print(key, h[key])
for key in sorted(h):
    print(key, h[key])