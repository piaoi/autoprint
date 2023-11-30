
import os
import time
import qrcode

date = time.strftime("%Y%m%d")
file_path = 'Y:\spu_'+date+'.log' # 文件路径
last_modified = os.stat(file_path).st_mtime  # 获取文件的修改时间
count = ''

#旧版计数器
try:   
    count = int(input('请输入当前产品序号：'))
    print("当前产品序列号为："+ str(count)) #代入
except ValueError:
    print('要输入整数哦')
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

                count += 1 #计数器加一

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
                print('不合格，跳过不打印')
                pass
        
    time.sleep(1)  # 延迟1秒后再次检查文件的修改时间