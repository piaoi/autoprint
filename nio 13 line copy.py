import os
import time

date = time.strftime("%Y%m%d")
file_path = 'Y:\spu_'+date+'.log' # 文件路径
last_modified = os.stat(file_path).st_mtime  # 获取文件的修改时间
count = 100

while True:
    # 检查文件的修改时间是否有变化
    if os.stat(file_path).st_mtime != last_modified:
        last_modified = os.stat(file_path).st_mtime
        with open(file_path, 'r') as file:
            file.seek(0)
            last_line = ''
            for line in file:
                last_line = line.rstrip()  # 去除行尾的换行符
           
            if " iO" in last_line: #前方加空格，防止nio干扰
                count += 1
                print(last_line)
                with open('output.txt', 'w') as file:  # 打开一个名为output.txt的文件进行写入操作
                    file.write(last_line + "--" +str(count))  # 将最后一行数据写入文件,加入计数器count.---3位占位符号
            else: 
                pass
        
    time.sleep(1)  # 延迟1秒后再次检查文件的修改时间