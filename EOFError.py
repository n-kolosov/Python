#!/usr/bin/python
# -*- coding: UTF-8 -*-
try:
    s = input("Введите данные: ")
    print(s)
except EOFError:
#Ошибка EOFError возникает, если при вводе данных нажать Ctrl + Z, а потом Enter
    print("Обработали исключение EOFError")