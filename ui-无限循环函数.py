
#导入所需库
from tkinter import *

#创建Tkinter窗口的实例
win=Tk()

#设置Tkinter窗口的大小
win.geometry("700x350")

#定义一个函数，在无限循环内打印一些东西
condition=True
def infinite_loop():
   if condition:
      Label(win, text="Infinite Loop!", font="Arial, 25").pack()

   # 1秒后调用infinite_loop() win.after(1000, infinite_loop)

def start():
   global condition
   condition=True

def stop():
   global condition
   condition=False

#创建一个按钮来开始无限循环
start = Button(win, text= "Start the Loop", font="Arial, 12", command=start).pack()
stop = Button(win, text="Stop the Loop", font="Arial, 12", command=stop).pack()

#每隔1秒钟调用infinite_loop函数
win.after(1000, infinite_loop)

win.mainloop()
