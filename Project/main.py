import Folder1.module1 as m1
print(m1.msg)
from Folder1 import module1 as m2
print(m2.msg)
from Folder1.module1 import msg
print(msg)

import Folder1.Folder2.module2 as m3
print(m3.msg)
from Folder1.Folder2 import module2 as m4
print(m4.msg)
from Folder1.Folder2.module2 import msg
print(msg)