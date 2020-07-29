# -*- coding: utf-8 -*-
"""
Created on Tue Jul 28 20:01:58 2020

@author: user
"""


'''
三角形的組成條件是任意兩邊加起來需大於第三邊；
請輸入三個數字來確定是否可以組成三角形，若是可以請輸出周長，
若是不行，請輸出無法組成三角形
'''
a,b,c, = eval(input("輸入三個數字:"))
if a >= b or a >= c :
    if a > b + c:
        print("無法組成三角形")
    else:
        print(a + b + c)

elif a < b or b >= c:
    if b > a + c:
        print("無法組成三角形")
    else:
        print(a + b + c)
elif c > a or c > b :
   if c > b + a:
        print("無法組成三角形")
   else:
        print(a + b + c)
    









