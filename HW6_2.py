# -*- coding: utf-8 -*-
"""
Created on Mon Jul 27 17:52:25 2020

@author: user
"""


#請輸入西元出生年，請以1900年後為主，輸入完後，會出現對應的生肖年，如: 1900年 為 老鼠。
print("歡迎來到不專業占卜")
year = eval(input("請輸入出生年份:"))
rem = year  % 12
if rem == 4:
    print("老鼠")
elif rem == 5:
    print("牛")
elif rem == 6:
    print("虎")
elif rem == 7:
    print("兔")
elif rem == 8:
    print("龍")
elif rem == 9:
    print("蛇")
elif rem == 10:
    print("馬")
elif rem == 11:
    print("羊")
elif rem == 3:
    print("你就是豬，對不?")
elif rem == 1:
    print("雞")
elif rem == 2:
    print("狗")
else:
    print("猴")
    