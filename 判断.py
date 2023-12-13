'''
Author: 木白广木林
Date: 2023-12-08 09:35:11
LastEditors: Do not edit
LastEditTime: 2023-12-08 09:44:40
FilePath: \py\判断.py
'''
# while True:
#     num = input("请输入一个正整数：")
#     if num.isdigit() and int(num) > 0:
#         print("您输入的正整数为：", num)
#         break
#     else:
#         print("请输入一个正整数！")
while True:
    num = input("请输入一个整数：")
    if num.isdigit() and int(num) > 0:
        print("您输入的是正整数：", num)
        pass
    elif num.isdigit() and int(num) == 0:
        print("您输入的是零")
        pass
    elif num.startswith('-') and num[1:].isdigit():
        print("您输入的是负整数：", num)
        pass
    else:
        print("请输入一个整数！")