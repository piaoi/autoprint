
# #!/usr/bin/env python3
# # -*- coding:utf-8 -*-
# # @FileName  :ch4_1_按键答应信息.py
# # @time      :2022/10/21 13:59
# # Author     :ming997



# """
# ch4_1 按键按下后显示需要打印的内容
# """
# from tkinter import *
# from PIL import Image, ImageTk

# def msgShow():
   
#     label["text"]="i love python"
#     label["bg"]="lightyellow"
#     label["fg"]="blue"
    
#     pass

# root = Tk()
# root.title("ch4_1") #窗口标题
# label = Label(root) #标签内容
# btn = Button(root,text="打印信息",command=msgShow)
# label.pack()
# btn.pack()

# root.mainloop()





# -*- coding:utf8 -*-

from tkinter import *

root = Tk()
root.title("Label Demo")


img = PhotoImage(file="--100.png")
stext = "人生苦短，我用Python"

# # 图片位于文字左侧
# label1 = Label(root, image=img, text=stext, compound="left", bg="lightyellow")
# label1.pack()

# # 图片位于文字右侧
# label2 = Label(root, image=img, text=stext, compound="right", bg="lightcyan")
# label2.pack()

# 图片位于文字上方
label3 = Label(root, image=img, text=stext, compound="top", bg="lightgreen")
label3.pack()

# # 图片位于文字下方
# label4 = Label(root, image=img, text=stext, compound="bottom", bg="lightgray")
# label4.pack()

# 文字覆盖图片中央，可做背景图片
# label5 = Label(root, image=img, text=stext, compound="center", bg="lightblue", fg="white", font=("微软雅黑", 24))
# label5.pack()

root.mainloop()


