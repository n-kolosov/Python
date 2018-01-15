import sys
print(sorted(sys.modules.keys()))
s = "test" + "s"
m = __import__(s)
print(m.x)