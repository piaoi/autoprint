'''
Author: 木白广木林
Date: 2023-11-29 10:45:20
LastEditors: Do not edit
LastEditTime: 2023-12-13 13:53:30
FilePath: \py\main-index.py
'''
'''
                       _oo0oo_
                      o8888888o
                      88" . "88
                      (| -_- |)
                      0\  =  /0
                    ___/`---'\___
                  .' \\|     |// '.
                 / \\|||  :  |||// \
                / _||||| -:- |||||- \
               |   | \\\  - /// |   |
               | \_|  ''\---/''  |_/ |
               \  .-\__  '-'  ___/-. /
             ___'. .'  /--.--\  `. .'___
          ."" '<  `.___\_<|>_/___.' >' "".
         | | :  `- \`.;`\ _ /`;.`/ - ` : | |
         \  \ `_.   \_ __\ /__ _/   .-` /  /
     =====`-.____`.___ \_____/___.-`___.-'=====
                       `=---='


     ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

           佛祖保佑     永不宕机     永无BUG

'''
# from itertools import count
import os
from tkinter import font
# import tkinter
from tracemalloc import start
import qrcode
import time
import datetime
from PIL import Image, ImageDraw, ImageFont,ImageWin
import win32print
import win32ui
#去除全局警告信息{控制台}
import warnings
warnings.filterwarnings("ignore")
###################################################################################################
from tkinter import *
from tkinter import Tk, Label
import tkinter as tk
from PIL import ImageTk, Image
import sys
#更改窗口图标
import ctypes
myappid = "auto.version" # 这里可以设置任意文本
ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID(myappid)

# Python中，在一个程序中，只能定义其中一种布局:pack\grid\place.

# stext =None
# image=None

#控制台输出
# class StdoutRedirector(object):
#     def __init__ (self, text_widget):
#         self.text_widget = text_widget
#     def write(self, str):
#         self.text_widget.insert(tk.END,str)
#         self.text_widget.see(tk.END)

# def show():

    # global image
    # global stext
    
    # image = Image.open("--100.png")
    # 使用Tkinter和ImageTk.PhotoImage可以将PIL库中的图像对象转换为Tkinter库能够接受的对象，
    # 并进行图像大小的调整
    # resize_image = image.resize((200,200))#规定图片大小
    # tkimg = ImageTk.PhotoImage(resize_image)

    # text = tk.Text(root,width= 50 ,height= 10)
    # text .pack()
    # #重定向标准输出
    # sys.stdout = StdoutRedirector(text)
    # print("Hello，world!") # 新出将会显示在文本框中
    # stext = "人生苦短，我用Python````````````````````"

    # # 图片位于文字左侧
    # label1 = Label(root, image=img, text=stext, compound="left", bg="lightyellow")
    # label1.pack()

    # # 图片位于文字右侧
    # label2 = Label(root, image=img, text=stext, compound="right", bg="lightcyan")
    # label2.pack()

    # 图片位于文字上方
    # label3 = Label(root, image=tkimg, text=stext,font=("宋体",25),fg="red", compound="top", bg="lightgreen")
    # label3.pack()

    # # 图片位于文字下方
    # label4 = Label(root, image=img, text=stext, compound="bottom", bg="lightgray")
    # label4.pack()

    # 文字覆盖图片中央，可做背景图片
    # label5 = Label(root, image=img, text=stext, compound="center", bg="lightblue", fg="white", font=("微软雅黑", 24))
    # label5.pack()
    # button.config(state=DISABLED)  #点击一次后失效

# def str():
#     image = Image.open("flush")
#我们声明了一个str隐藏内置str类的函数。
#当我们调用str()时，我们实际上是在调用我们自己的函数，而不是内置类。
# 确保您没有与内置函数共享相同名称的函数。
#############血的教训！！！！！！！！！！！！！！！！！！！！！！！！




#控制台输出
class ConsoleRedirector:
    def __init__(self, text_widget):
        self.text_widget = text_widget
        self.text_widget.see(tk.END)

    def write(self, message):
        self.text_widget.insert(tk.END, message)
    
    def flush(self):        # 这情况下, 不需要作任何事sys.stdout 需要一个类似文件的对象，现在指定为 Logger 对象，它会调用它的 write 以及 flush 方法，事实上，Logger 确实没有定义 flush 方法.
        pass
 

# 二维码储存路径
path1=r'E:\360MoveData\Users\bai\Desktop\py\XXX'
# 年-月-日 时：分：秒
now_time1 = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
   # 年
year1 = datetime.datetime.now().strftime('%Y')
   # 年-月
month1 = datetime.datetime.now().strftime('%Y-%m')
   # 年-月-日
day1 = datetime.datetime.now().strftime('%Y-%m-%d')
foldername1 ="\\"+year1+"\\"+month1+"\\"+day1

#图片拼接
def comb(png1, png2, style='horizontal'):

    img1, img2 = Image.open(png1), Image.open(png2)
    # 统一图片尺寸，可以自定义设置（宽，高）
    img1 = img1.resize((570, 200), Image.ANTIALIAS) #以第一张图片高度为准
    img2 = img2.resize((100, 100), Image.ANTIALIAS)
    size1, size2 = img1.size, img2.size
    if style == 'horizontal':
        joint = Image.new('RGB', (size1[0] + size2[0], size1[1]))
        loc1, loc2 = (0, 0), (25, 50)
        joint.paste(img1, loc1)
        joint.paste(img2, loc2)
        joint.save('putout.png')

    elif style == 'vertical':
        joint = Image.new('RGB', (size1[0], size1[1] + size2[1]))
        loc1, loc2 = (0, 0), (50,0)
        joint.paste(img1, loc1)
        joint.paste(img2, loc2)
        joint.save('putout1.png')

#每日新建文件夹
def create_folder(path):  #创建函数
   # 年-月-日 时：分：秒
   now_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
   # 年
   year =datetime.datetime.now().strftime('%Y')
   # 年-月
   month = datetime.datetime.now().strftime('%Y-%m')
   # 年-月-日
   day = datetime.datetime.now().strftime('%Y-%m-%d')
   # 时：分：秒
#    hour = datetime.datetime.now().strftime("%H:%M:%S")
#    print(now_time + "\n"+day + "\n" + hour)
   foldername = path+"\\"+year+"\\"+month+"\\"+day
   # print(pwd)
   # 文件路径
   word_name = os.path.exists(foldername)
   # 判断文件是否存在：不存在创建
   if not word_name:
       os.makedirs(foldername)

#计数
def update_label():
    # 更新标签内容
    global counta
    counta += 1
    label.config(text="当前计数为Count: {}".format(counta),font=("宋体",15),fg="red")
    

#检测更新二维码并展示
class ImageDisplayApp:
    def __init__(self, root, image_folder):
        self.root = root
        self.image_folder = image_folder
        self.image_label = tk.Label(root)
        self.image_label.pack()
        self.update_image()

    def update_image(self):
        image_files = [f for f in os.listdir(self.image_folder) if f.endswith('.png') or f.endswith('.jpg')]
        if image_files:
            latest_image = max(image_files, key=lambda x: os.path.getctime(os.path.join(self.image_folder, x)))
            image_path = os.path.join(self.image_folder, latest_image)

            #更改图片大小
            image = Image.open(image_path)
            resize_image = image.resize((200,200))  
            photo = ImageTk.PhotoImage(resize_image)

            self.image_label.configure(image=photo)
            self.image_label.image = photo

        self.root.after(1000, self.update_image)  # 每隔1秒检测一次

class MainPage(tk.Tk):
    def __init__(self):
        super().__init__()
        self.iconphoto(True, tk.PhotoImage(file='QQmain.png'))
        self.set_ui()

#运行主函数
date = time.strftime("%Y%m%d")  #路径时间字符
dateout = time.strftime("%m-%d-%HH") #打印时间字符
file_path = 'Y:\spu_'+ date +'.log' # 数据读取文件路径（文件名字）
last_modified = os.stat(file_path).st_mtime  # 获取文件的修改时间
# count = ''

def main():
    global last_modified #嵌套函数全局声明
    global date
    global dateout
    global file_path
    global count
    
    # print("程序监听")

    if os.stat(file_path).st_mtime != last_modified:
        last_modified = os.stat(file_path).st_mtime
        with open(file_path, 'r') as file:
            file.seek(0)
            last_line = ''
            line1 = ''
            for line in file:
                last_line = line.rstrip()  # 去除行尾的换行符
           
            if " iO" in last_line: #前方加空格，防止nio干扰
                
                count += 1 #计数器循环加一

                print(last_line)
                # print(count)
                with open('output.txt', 'w') as file:  # 打开一个名为output.txt的文件进行写入操作
                    file.write(last_line + "----" + str(count))  # 将最后一行数据写入文件,加入计数器count.---3位占位符号
                
                line1 = last_line + "----" + str(count)  #将最后一行数据写入line1 ，否则需要再次读写文件嵌套

                # print(line1) #增加序号后的一行数据

                #二维码输出
                qr = qrcode.QRCode(
                version=2,
                error_correction=qrcode.constants.ERROR_CORRECT_L,
                box_size=10,
                border=1
                )#设置二维码的大小

                # qr.add_data(last_line)
                qr.add_data(line1)
                qr.make(fit=True)
                img = qr.make_image()
                line2=line1[-5:] #取后5位命名

                print(line2) #二维码命名后缀
                
                img.save(path + foldername1 + '/' + line2 + ".png") #图片命名  '/'非常重要; 绝对路径‘\\’
                
                if __name__ == '__main__':
                # 两张图片地址：
                    # png1 = r"./--100.png"
                    png2 = path + foldername1 + '/' + line2 + ".png"
                    png1 = r"./99999.png"
                    # 左右拼接
                    comb(png1, png2, style='horizontal')

                    # 上下拼接
                    # comb(png1, png2, style='vertical')
    
                    # 打开图片
                    image = Image.open('putout.png')

                    # 在右侧添加文字
                    draw = ImageDraw.Draw(image)
                    text = dateout + " No." + line2
                    font = ImageFont.truetype('arial.ttf', 30)  # 修改字体和大小
                    text_width, text_height = draw.textsize(text, font)
                    x = image.width - text_width - 280  # 文字位置，可以自行调整
                    y = image.height // 2 - text_height // 2
                    draw.text((x, y), text, font=font, fill='red')
                    # draw.text((x, y), text, font=font, fill='white')

                    # 显示图片
                    # image.show() #防止跳出循环不进行打印

                    # 保存图片
                    image.save('final.png')

                    # 使用打印机打印图片
                    # 列出所有打印机
                    # printers = [printer[2] for printer in win32print.EnumPrinters(2)]
                    # for i, printer in enumerate(printers):
                    #     print(f"{i+1}: {printer}")

                    # 选择打印机
                    # choice = int(input("选择要使用的打印机 (输入对应的序号): ")) - 1
                    # printer_name = printers[choice]

                    # 不选则，直接获取默认打印机
                    printer_name = win32print.GetDefaultPrinter()


                    # 加载图片
                    image_path = r"final.png"
                    image = Image.open(image_path)

                    # 创建设备描述表
                    hDC = win32ui.CreateDC()
                    hDC.CreatePrinterDC(printer_name)

                    # 开始文档
                    hDC.StartDoc(image_path)

                    # 开始页面
                    hDC.StartPage()

                    # 绘制位图
                    dib = ImageWin.Dib(image)
                    dib.draw(hDC.GetHandleOutput(), (0, 0, image.width, image.height))

                    # 结束页面
                    hDC.EndPage()

                    # 结束文档
                    hDC.EndDoc()

                    # 删除设备描述表对象
                    del hDC
                    print("打印成功！")
                    update_label()
            elif " ST" in last_line: #前方加空格，防止nio干扰       #if与多个else if是分枝情况。只执行其中一条代码，只要第一个if条件成立，即使满足else if的条件也不会执行elseif及else的内容
                                                                   # if与多个if是并列情况，会顺序执行
                print(last_line) #添加不合格不合法数据
                print('不合法,跳过不打印')
                pass
            else: 
                print(last_line) #添加不合格不合法数据
                print('不合格，不打印')
                pass
    # time.sleep(1)  # 延迟1秒后再次检查文件的修改时间
    root.after(1000, main)
    
    # print("程序结束")

#主窗口
# if __name__=='__main__':
#    path=r'E:\360MoveData\Users\bai\Desktop\py\XXX' # 文件夹建立位置
#    create_folder(path) #每日按日期新建文件夹
if __name__ == "__main__":
    path=r'E:\360MoveData\Users\bai\Desktop\py\XXX' # 文件夹建立位置
    create_folder(path) #每日按日期新建文件夹

    # 创建窗口：实例化一个窗口对象。
    root = Tk()
    
    # 窗口居中
    screenWidth = root.winfo_screenwidth()  # 获取显示区域的宽度
    screenHeight = root.winfo_screenheight()  # 获取显示区域的高度
    width = 700  # 设定窗口宽度
    height = 550  # 设定窗口高度
    left = (screenWidth - width) / 2
    top = (screenHeight - height) / 2
    # 宽度x高度+x偏移+y偏移
    # 在设定宽度和高度的基础上指定窗口相对于屏幕左上角的偏移位置
    root.geometry("%dx%d+%d+%d" % (width, height, left, top))
    # root.geometry("700x550+374+182")  #root.geometry("600x400+374+182")调整窗口的大小+位置；
    
    #  窗口标题
    root.title("蔚来13线自动标签系统--木白广木林个人测试版")
    # root.iconbitmap('QQmain.ico') # 更改窗口图标
    root.tk.call('wm', 'iconphoto', root._w, tk.PhotoImage(file='QQmain.png'))  #更改窗口图标

    # root.state("zoomed") #全屏
    # root.resizable(0, 0)  # 禁止窗口调整大小
    
    # 添加标签控件
    # label = Label(root,text="请输入当前产品序号：",font=("宋体",25),fg="red")
    # 定位
    # label.grid(row=2,column=1)
    # label.pack()
    
    # 添加输入框
    # entry = Entry(root,font=("宋体",25),fg="red")
    # entry.grid(row=2,column=2)
    # entry.pack()
    
    # 添加点击按钮
    # button = Button(root,text="确定",font=("宋体",25),fg="blue",command=show)
    # button = Button(root,text="确定",font=("宋体",25),fg="blue")
    # button.grid(row=3,column=2)
    # button.pack()

    #文本传参
    entry_var = tk.StringVar()
    label = Label(root,text="请输入当前产品序号：",font=("宋体",25),fg="red").pack()  # 添加标签控件
    entry = tk.Entry(root,font=("宋体",25),fg="red",width= 25,textvariable=entry_var) # 添加输入框
    entry.pack()
    # entry_var.set('')
    def start():

        global count
        # entry.configure(state='readonly') 
        num = entry.get()		# 调用get()方法，将Entry中的内容获取出来
        # print(num)
        # 我们可以用控件的configure方法修改控件的属性，设置控件状态的属性就是state
        # num = input("请输入当前产品序号：")
        if num.isdigit() and int(num) > 0:
            print("您输入当前产品序列号为：", num)
            count = int(num)
            count-= 1 #初始值减一，下方循环加一
            entry.configure(state='readonly') #输入正确后不可修改
            button.config(state='disable') #输入正确后不可再次提交
            # print(count)

            # main()  #主函数
            root.after(1000, main())
            
            # break
        elif num.isdigit() and int(num) == 0:
            print("您输入的是零,序列号不为0！")
            text.see(END) #Text 保持焦点在行尾
            pass
        elif num.startswith('-') and num[1:].isdigit():
            print("您输入的是负整数,序列号不为负数！")
            text.see(END) #Text 保持焦点在行尾
            pass
        else:
            print("请输入一个整数！序列号不为字符！")
            text.see(END) #Text 保持焦点在行尾
            pass
        
    button = tk.Button(root,text="确定",font=("宋体",25),fg="blue",command=start)
    button.pack()

    # app = ImageDisplayApp(root, r"E:\360MoveData\Users\bai\Desktop\py\XXX")  #检测更新图片文件夹路径
    app = ImageDisplayApp(root, path + foldername1)  #检测更新图片文件夹路径

    #计数
    label = tk.Label(root, text="当前计数Count: 0",font=("宋体",15),fg="red")
    label.pack()
    counta = 0
    # update_label()

    s1 = Scrollbar(root)
    s1.pack(side = RIGHT, fill = Y)
    # HORIZONTAL 设置水平方向的滚动条，默认是竖直
    # s2 = Scrollbar(root, orient = HORIZONTAL)
    # s2.pack(side = BOTTOM, fill = X)
    # 创建文本框
    # wrap 设置不自动换行
    # text = tk.Text(root,width= 20 ,height= 10, yscrollcommand = s1.set, xscrollcommand = s2.set, wrap = 'none')
        # wrap属性有三个可选值：tk.NONE：不换行tk.CHAR：按字符换行tk.WORD：按单词换行
    text = tk.Text(root,width= 80 ,height= 10, yscrollcommand = s1.set,wrap = tk.WORD)
    # text.pack(expand = YES,fill = BOTH)
    text.pack(expand = YES,fill = Y)
    s1.config(command =text.yview)
    # s2.config(command =text.xview)

    sys.stdout = ConsoleRedirector(text)

    print("////////////////////////////////////程序开始运行////////////////////////////////")

    root.mainloop()

 ##############################################################################

# 显示窗口
# root.mainloop()