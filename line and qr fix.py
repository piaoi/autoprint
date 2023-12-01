'''
Author: 木白广木林
Date: 2023-11-29 10:45:20
LastEditors: Do not edit
LastEditTime: 2023-11-30 10:43:10
FilePath: \py\line and qr fix.py
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

       佛曰:  
               写字楼里写字间，写字间里程序员；  
               程序人员写程序，又拿程序换酒钱。  
               酒醒只在网上坐，酒醉还来网下眠；  
               酒醉酒醒日复日，网上网下年复年。  
               但愿老死电脑间，不愿鞠躬老板前；  
               奔驰宝马贵者趣，公交自行程序员。  
               别人笑我忒疯癫，我笑自己命太贱；  
               不见满街漂亮妹，哪个归得程序员？
'''

import os
import time
import qrcode

date = time.strftime("%Y%m%d")
file_path = 'Y:\spu_'+date+'.log' # 文件路径
last_modified = os.stat(file_path).st_mtime  # 获取文件的修改时间
count = ''

#旧版计数器
# try:   
#     count = int(input('请输入当前产品序号：'))
#     print("当前产品序列号为："+ str(count)) #代入
# except ValueError:
#     print('要输入整数哦')
#     pass

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

                img.save(line2+".png")

            else: 
                print('不合格不合法，跳过不打印')
                pass
        
    time.sleep(1)  # 延迟1秒后再次检查文件的修改时间