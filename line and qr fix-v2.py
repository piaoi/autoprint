'''
Author: 木白广木林
Date: 2023-11-29 10:45:20
LastEditors: Do not edit
LastEditTime: 2023-11-30 17:01:25
FilePath: \py\line and qr fix-v2.py
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

import os
import qrcode
import time
import datetime

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
if __name__=='__main__':
   path=r'E:\360MoveData\Users\bai\Desktop\py\XXX' # 文件夹建立位置
   create_folder(path) #每日按日期新建文件夹

date = time.strftime("%Y%m%d")
file_path = 'Y:\spu_'+ date +'.log' # 数据读取文件路径
last_modified = os.stat(file_path).st_mtime  # 获取文件的修改时间
count = ''

#新版计数器
while True:
    # print('请输入当前产品序号：') #input不可连接中文
    count = int(input('请输入当前产品序号：'))
    try:
        if int(count)>0:
                print('当前产品序列号为：' + str(count))
                count-= 1 #初始值减一，下方循环加一
                break
        if int(count)<0:
                print('序列号不为负数！')
                pass
        if int(count) == 0:   #=0不合语法
                print('序列号不为0！')
                pass
    except:
        print('请输入整数!')
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
                    file.write(last_line + "----" +str(count))  # 将最后一行数据写入文件,加入计数器count.---3位占位符号
                
                line1 = last_line + "----" +str(count) #将最后一行数据写入line1 ，否则需要再次读写文件嵌套

                print(line1) #增加序号后的一行数据

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

            else: 
                print('不合法跳过,不合格不打印')
                pass
        
    time.sleep(1)  # 延迟1秒后再次检查文件的修改时间