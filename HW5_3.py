# -*- coding: utf-8 -*-
"""
Created on Tue Jul 14 11:05:03 2020

@author: user
"""


#請建立一個空白文字檔，可輸入姓名，生日，年齡如下圖格式
fstream = open('C:\python123\out5.txt',mode ="x")
name = input("請輸入姓名:")
birthday = input("請輸入生日:")
age = input("請輸入年齡:")
fstream = name(str) + birthday(str) + age(str)
print(fstream ,file = fstream)
fstream.close()
