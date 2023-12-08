

from email.mime import image
from tkinter import *
from tkinter import Tk, Label
from PIL import ImageTk, Image
import logging


# Python中，在一个程序中，只能定义其中一种布局:pack\grid\place.


stext =None
image=None



def func():
    print("序号为" + stext)
    button.config(state=Tk.DISABLED)  #点击一次后失效

def show():

    global image
    global stext
    
    image = Image.open("--100.png")
    #使用Tkinter和ImageTk.PhotoImage可以将PIL库中的图像对象转换为Tkinter库能够接受的对象，
    # 并进行图像大小的调整
    resize_image = image.resize((200,200))
    tkimg = ImageTk.PhotoImage(resize_image)
    # photo = ImageTk.PhotoImage(image)  # 用PIL模块的PhotoImage打开 
    # image = image.resize((200,200))    #规定图片大小
    # imglabel = Label(root, image=photo)
    imglabel = Label(root, image=tkimg)
    # imglabel.image = photo   #保留对图片的引用
    imglabel.image = tkimg   #保留对图片的引用
    # imglabel.config(background='red')  #背景颜色
    # imglabel.grid(row=0, column=2, columnspan=3)
    stext = "人生苦短，我用Python````````````````````"

    # # 图片位于文字左侧
    # label1 = Label(root, image=img, text=stext, compound="left", bg="lightyellow")
    # label1.pack()

    # # 图片位于文字右侧
    # label2 = Label(root, image=img, text=stext, compound="right", bg="lightcyan")
    # label2.pack()

    # 图片位于文字上方
    label3 = Label(root, image=tkimg, text=stext,font=("宋体",25),fg="red", compound="top", bg="lightgreen")
    label3.pack()

    # # 图片位于文字下方
    # label4 = Label(root, image=img, text=stext, compound="bottom", bg="lightgray")
    # label4.pack()

    # 文字覆盖图片中央，可做背景图片
    # label5 = Label(root, image=img, text=stext, compound="center", bg="lightblue", fg="white", font=("微软雅黑", 24))
    # label5.pack()
    button.config(state=DISABLED)  #点击一次后失效
# btn = Button(root, text="show", command=show)
# btn.grid(row=0, column=1)
 
# 创建窗口：实例化一个窗口对象。
root = Tk()
 
# 窗口居中
screenWidth = root.winfo_screenwidth()  # 获取显示区域的宽度
screenHeight = root.winfo_screenheight()  # 获取显示区域的高度
width = 600  # 设定窗口宽度
height = 400  # 设定窗口高度
left = (screenWidth - width) / 2
top = (screenHeight - height) / 2
# 宽度x高度+x偏移+y偏移
# 在设定宽度和高度的基础上指定窗口相对于屏幕左上角的偏移位置
root.geometry("%dx%d+%d+%d" % (width, height, left, top))
# root.geometry("700x550+374+182")  #root.geometry("600x400+374+182")调整窗口的大小+位置；
 
#  窗口标题
root.title("蔚来13线--个人版")

# root.state("zoomed") #全屏

#开屏封面图片
# image = Image.open("99999.png")
# image = image.resize((100,100))    #规定图片大小
# pyt = ImageTk.PhotoImage(image)
# label = Label(root, image=pyt)
# label.grid(row=0,column=2)

 
# 添加标签控件
label = Label(root,text="序号：",font=("宋体",25),fg="red")
# 定位
# label.grid(row=2,column=1)
label.pack()
 
# 添加输入框
entry = Entry(root,font=("宋体",25),fg="red")
# entry.grid(row=2,column=2)
entry.pack()
 
# 添加点击按钮
button = Button(root,text="确定",font=("宋体",25),fg="blue",command=show)
# button.grid(row=3,column=2)
button.pack()

"""
command=func表示调用最开始定义的func函数。
func函数一定要在这句代码之前，因为这里需要调用这个func函数。
"""


# 显示窗口
root.mainloop()