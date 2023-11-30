# print('你选择你最喜欢的明星：1：刘德虎 2：吴彦祖')
# choice = input('请输入您的选择：')
# #变量赋值

# if choice == '1':
# #条件判断:条件1
#     print('刘德华，我喜欢你')
# #条件1的结果

# else:
# #条件判断：其他条件
#     print('吴彦祖，我喜欢你')
# #其他条件的结果
# 

while True:
    i = input("请输入产品序号：")
    try:
        if int(i)>0:
                print(i)
                break
        if int(i)<0:
                print('序列号不为负数！')
                pass
        if int(i) == 0:
                print('序列号不为0！')
                pass
    except:
        print('请输入整数!')
        pass