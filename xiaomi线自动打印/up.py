
'''0127-1200066-20231228-0000'''
# import time

# def increment_last_number(file_path):
#     while True:
#         with open(file_path, 'r+') as file:
#             content = file.read().strip()
#             if content and content[-1].isdigit():
#                 last_digit = int(content[-1])
#                 new_content = content[:-1] + str(last_digit + 1)
#                 file.seek(0)
#                 file.truncate()
#                 file.write(new_content)
#                 print(f"Updated content: {new_content}")
#             else:
#                 print("No digit found at the end of the file.")
#         time.sleep(5)

# file_path = r'E:\360MoveData\Users\bai\Desktop\autoprint-xiaomi\output.txt'  # 替换为您的文件路径
# increment_last_number(file_path)
import time

def update_file():
    filename = 'output.txt'  # 更改为您的文件名

    while True:
        with open(filename, 'r+') as file:
            content = file.read().strip()
            if content:
                last_four_digits = content[-4:]  # 获取文本末尾的4位数字
                new_number = str(int(last_four_digits) + 1).zfill(4)  # 对末尾数字加一并保持4位数格式
                updated_content = content[:-4] + new_number  # 更新文件内容
                file.seek(0)
                file.truncate()
                file.write(updated_content)
                print(f"{updated_content}")

        time.sleep(5)  # 暂停5秒钟再执行下一次更新

# 运行更新函数
update_file()
