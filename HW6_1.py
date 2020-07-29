# -*- coding: utf-8 -*-
"""
Created on Mon Jul 27 17:52:24 2020

@author: user
"""


#請先輸入A、B來選擇轉換成華氏或攝氏溫度，輸入該溫度後再轉成對應的華氏或 攝氏溫度(依據你的選項)
input1 = input("攝氏轉華氏請輸入A，華氏轉攝氏請輸入B:)")
input2 = eval(input("請輸入溫度:"))
if input1 == "A":
    input2 = (input2 + 32) * 9 / 5
    
else :
    input2 = (input2 - 32) * 5 / 9
print(input2)