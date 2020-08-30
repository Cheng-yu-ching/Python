# -*- coding: utf-8 -*-
"""
Created on Fri Aug 28 21:16:53 2020

@author: user
"""


accounts = [ ]
account = input("建立帳號:")
accounts.append(account)
s = 1
while s == 1:
    account1 = input("輸入帳號:")
    if account1 in accounts:
        print("歡迎進入系統")
        s = 0
    else:       
        print("輸入錯誤")