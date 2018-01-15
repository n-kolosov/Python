import time
print(time.time())
print(time.gmtime())
t = time.time() - 100000000
print(time.gmtime(t))