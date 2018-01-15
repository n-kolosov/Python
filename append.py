#!/usr/bin/python
# -*- coding: UTF-8 -*-
#оператор append добавляет один объект в конец массива
arr = [1, 2, 3]
arr.append(4) #добавляем число в массив
print(arr)
arr.append([5, 6])
print(arr) #добавляем вложенный массив в массив
arr.append((7, 8)) #добавляем кортеж в массив
print(arr)