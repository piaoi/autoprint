import os
import time

date = time.strftime("%Y%m%d")
file_path = 'Y:\spu_'+date+'.log' # 文件路径
last_modified = os.stat(file_path).st_mtime  # 获取文件的修改时间

while True:
    # 检查文件的修改时间是否有变化
    if os.stat(file_path).st_mtime != last_modified:
        last_modified = os.stat(file_path).st_mtime
        with open(file_path, 'r') as file:
            file.seek(0)
            last_line = ''
            for line in file:
                last_line = line.rstrip()  # 去除行尾的换行符
           
            if "iO" in last_line:
                print(last_line)
                with open('output.txt', 'w') as file:  # 打开一个名为output.txt的文件进行写入操作
                    file.write(last_line)  # 将最后一行数据写入文件
            else:
                pass
        
    time.sleep(1)  # 延迟1秒后再次检查文件的修改时间