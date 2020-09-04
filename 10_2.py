# -*- coding: utf-8 -*-
"""
Created on Tue Sep  1 22:55:32 2020

@author: user
"""


k = {}
e = 1
while e == 1:
    name = input("姓名")
    score = input("成績")
    k[name] = score
    m = input("是否離開")
    if m == 'Q':
        e = 0


