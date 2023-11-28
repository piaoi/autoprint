import time
import datetime
 
# def sleeptime(hour, min, sec):
#     return hour * 3600 + min * 60 + sec
date = time.strftime("%Y%m%d")
data = []  # 创建一个空列表
with open('Y:\spu_'+date+'.log', 'r') as file:  # 打开文件进行读取
    for line in file:  # 按行读取文件
        data.append(line.strip())  # 将每一行数据添加到列表中，并去除行末的换行符

last_line = data[-1]  # 使用索引-1获取列表中的最后一个元素

print(last_line)  # 输出最后一行数据到屏幕

with open('output.txt', 'w') as file:  # 打开一个名为output.txt的文件进行写入操作
    file.write(last_line)  # 将最后一行数据写入文件


# second = sleeptime(0, 0, 1)
# while 1 == 1:
#     time.sleep(second)
#     print(last_line)
# 这是隔5秒执行一次

if __name__ == '__main__':
    path = r'Y:\spu_'+date+'.log'
    file = open(path)
while True:
    where = file.tell()
    line = file.readline()
    if not line: ##等价于if line == "":
        time.sleep(1)
        file.seek(where)
    else:
        print(line, end='')

# with open('file_path', 'r') as f:
    # last_line = ''  # 记录最后一行内容的变量
    # for line in f:  # 逐行读取文件数据
    #     last_line = line  # 记录每一行的内容，直到读取到最后一行
    # print(last_line)  # 打印最后一行的内容