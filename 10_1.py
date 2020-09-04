# -*- coding: utf-8 -*-
"""
Created on Tue Sep  1 22:23:05 2020

@author: user
"""


en_ch = {'Monday':'星期一','Tuesday':'星期二','Wednesday':'星期三',
         'Thursday':'星期四','Friday':'星期五','Saturday':'星期六',
         'Sunday':'星期日'}
nn = str(input("輸入欲查詢詞:"))
if nn not in en_ch:
    print("輸入錯誤")

elif nn in en_ch:
    abc = en_ch[nn]
    print(abc)


