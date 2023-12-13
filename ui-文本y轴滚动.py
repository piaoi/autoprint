
#!/usr/bin/python
#coding: utf-8
 
from tkinter import *
import tkinter as tk
 
root = Tk()
root.title("记事本")
root.geometry("280x260+100+100")
 
s1 = Scrollbar(root)
s1.pack(side = RIGHT, fill = Y)
# HORIZONTAL 设置水平方向的滚动条，默认是竖直
s2 = Scrollbar(root, orient = HORIZONTAL)
s2.pack(side = BOTTOM, fill = X)
 
 
# 创建文本框
# wrap 设置不自动换行
textpad = Text(root, width = 200, yscrollcommand = s1.set, xscrollcommand = s2.set, wrap = 'none')
textpad.pack(expand = YES,fill = BOTH)
 
s1.config(command = textpad.yview)
s2.config(command = textpad.xview)
        
 
root.mainloop()