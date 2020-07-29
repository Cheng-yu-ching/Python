# -*- coding: utf-8 -*-
"""
Created on Mon Jul 27 17:52:27 2020

@author: user
"""


#請輸入三個數字，並由程式將他由大排到小
a,b,c, = eval(input("輸入三個數字:"))
if a >= b and b >= c:
    print(a)
    print(b)
    print(c)
elif a >= c and b <= c:
    print(a)
    print(c)
    print(b)
elif a < b and a >= c:
    print(b)
    print(a)
    print(c)
elif a < c and b >= c:
    print(b)
    print(c)
    print(a)
elif c>b>a:
    print(c)
    print(b)
    print(a)
elif c > a >= b:
    print(c)
    print(a)
    print(b)
    
    