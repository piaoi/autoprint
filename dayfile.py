'''
Author: 木白广木林
Date: 2023-11-30 10:51:23
LastEditors: Do not edit
LastEditTime: 2023-11-30 10:54:30
FilePath: \py\dayfile.py
'''
import os
folder=r'E:\360MoveData\Users\bai\Desktop\py\Day'   #这个是所需要创建的文件夹的根目录
for i in range(1,10):   #range函数是典型的左闭右开
    path=folder+'\\'+'Day'+'_'+str(i)    #这是你所需要创建的文件夹的目录名称 以Day_1，Day_2，Day_3.....等依次命名
    if os.path.exists(path)==False: #判断你要创建的文件夹是否已经存在，如果==False，是不存在，则创建该文件夹。否则不创建。
        os.makedirs(path)
