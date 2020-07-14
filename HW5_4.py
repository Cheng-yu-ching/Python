# -*- coding: utf-8 -*-
"""
Created on Tue Jul 14 09:50:10 2020

@author: user
"""


#輸入一個等差數列的連續前四個數字後，會計算出第五個數字
n1,n2,n3,n4= eval(input("請輸入等差數列前四項:"))
n5 = 2 * int(n4) - int(n3)
print(n1,n2,n3,n4,n5)
