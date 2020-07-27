# -*- coding: utf-8 -*-
"""
Created on Tue Jul 14 09:52:23 2020

@author: user
"""


#請建立一個任意文字檔，可重複用程式開啟輸入資料，每次輸入完後會換行。原內容不會被刪除。
fstream = open("c:\python123\新文字文件.txt", mode = "a")
information = input("輸入文字:")
print(information ,file= fstream)
fstream.close()
