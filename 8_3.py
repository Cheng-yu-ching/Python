# -*- coding: utf-8 -*-
"""
Created on Sun Aug 30 11:03:40 2020

@author: user
"""

n1 = int(input())
n2 = int(input())
n3 = int(input())
n4 = int(input())
n5 = int(input())

listnum = []
listnum.append(n1)
listnum.append(n2)
listnum.append(n3)
listnum.append(n4)
listnum.append(n5)
maxnum = max(listnum)
minnum = min(listnum)
listnum_sorted = sorted(listnum)
print(listnum_sorted)
print(maxnum)
print(minnum)

