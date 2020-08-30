# -*- coding: utf-8 -*-
"""
Created on Sun Aug 30 10:59:35 2020

@author: user
"""


w = input()
if 'http://' in w:
    print("是網址")
elif 'https://' in w:
    print("是網址")
else:
    print("不是網址")