#!/usr/bin/python3.6
# -*- coding: UTF-8 -*-
arr = [1, 2, 3]
def ins(x, y):
    arr.insert(x, y) #вставляет элемент в конкретное место в массиве. Первый аргумент - позиция, второй - элемент
    print(arr)
ins(0, 0)
ins(4, 4)
ins(5, 100)

arr = [1, 2, 3]
arr[:0] = [-2, -1, 0]
print(arr)
