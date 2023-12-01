'''
Author: 木白广木林
Date: 2023-11-30 10:56:06
LastEditors: Do not edit
LastEditTime: 2023-11-30 10:58:00
FilePath: \py\timefile.py
'''
# _*_coding:utf-8_*_
import os
import datetime
def create_folder(path):
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
   path=r'E:\360MoveData\Users\bai\Desktop\py\Day' # 文件夹建立位置
   create_folder(path)