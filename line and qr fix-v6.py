'''
Author: 木白广木林
Date: 2023-11-29 10:45:20
LastEditors: Do not edit
LastEditTime: 2023-12-12 12:51:09
FilePath: \py\line and qr fix-v6.py
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
import qrcode
import time
import datetime
from PIL import Image, ImageDraw, ImageFont,ImageWin
import win32print
import win32ui
#去除全局警告信息{控制台}
import warnings
warnings.filterwarnings("ignore")

# 二维码储存路径
path1=r'E:\360MoveData\Users\bai\Desktop\py\XXX'
# 年-月-日 时：分：秒
now_time1 = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
   # 年
year1 =datetime.datetime.now().strftime('%Y')
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

date = time.strftime("%Y%m%d")  #路径时间字符
dateout = time.strftime("%m-%d-%HH") #打印时间字符
file_path = 'Y:\spu_'+ date +'.log' # 数据读取文件路径
last_modified = os.stat(file_path).st_mtime  # 获取文件的修改时间
# count = ''

if __name__=='__main__':
   path=r'E:\360MoveData\Users\bai\Desktop\py\XXX' # 文件夹建立位置
   create_folder(path) #每日按日期新建文件夹

#新版计数器v2
# while True:
#     # print('请输入当前产品序号：') #input不可连接中文
#     count = input('请输入当前产品序号：')
#     try:
#         if int(count)>0:
#                 print('当前产品序列号为：' + str(count))
#                 count-= 1 #初始值减一，下方循环加一
#                 break
#         if int(count)<0:
#                 print('序列号不为负数！')
#                 pass
#         if int(count) == 0:   #=0不合语法
#                 print('序列号不为0！')
#                 pass
#     except:
#         print('请输入一个正整数!')
#         pass
    # 示例:计数器v3
while True:
    num = input("请输入当前产品序号：")
    if num.isdigit() and int(num) > 0:
        print("您输入当前产品序列号为：", num)
        count = int(num)
        count-= 1 #初始值减一，下方循环加一
        break
    elif num.isdigit() and int(num) == 0:
        print("您输入的是零,序列号不为0！")
        pass
    elif num.startswith('-') and num[1:].isdigit():
        print("您输入的是负整数,序列号不为负数！")
        pass
    else:
        print("请输入一个整数！序列号不为字符！")
        pass

while True:
    # 检查文件的修改时间是否有变化
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
                with open('output.txt', 'w') as file:  # 打开一个名为output.txt的文件进行写入操作
                    file.write(last_line + "----" + str(count))  # 将最后一行数据写入文件,加入计数器count.---3位占位符号
                
                line1 = last_line + "----" + str(count) #将最后一行数据写入line1 ，否则需要再次读写文件嵌套

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
            elif " ST" in last_line: #前方加空格，防止nio干扰       #if与多个else if是分枝情况。只执行其中一条代码，只要第一个if条件成立，即使满足else if的条件也不会执行elseif及else的内容
                                                                   # if与多个if是并列情况，会顺序执行
                print(last_line) #添加不合格不合法数据
                print('不合法,跳过不打印')
                pass
            else: 
                print(last_line) #添加不合格不合法数据
                print('不合格，不打印')
                pass
    time.sleep(1)  # 延迟1秒后再次检查文件的修改时间