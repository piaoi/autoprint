# from tkinter import *

# from PIL import ImageTk

# root = Tk()

# numIdx = 6
# frames = [ImageTk.PhotoImage(file='./data/'+str(i)+'.jpg') for i in range(1,7)]


# def update(idx):  # 定时器函数
#     frame = frames[idx]
#     idx += 1  # 下一帧的序号：在0,1,2,3,4,5之间循环(共6帧)
#     label.configure(image=frame)  # 显示当前帧的图片
#     root.after(1000, update, idx % numIdx)  # 0.1秒(100毫秒)之后继续执行定时器函数(update)


# label = Label(root)
# label.pack()
# root.after(1000, update, 0)  # 立即启动定时器函数(update)
# root.mainloop()
# # ``````````````````````````````````````````````

import os
import time
import tkinter as tk
from PIL import Image, ImageTk

class ImageDisplayApp:
    def __init__(self, root, image_folder):
        self.root = root
        self.image_folder = image_folder
        self.image_label = tk.Label(root)
        self.image_label.pack()

        self.update_image()

    def update_image(self):
        image_files = [f for f in os.listdir(self.image_folder) if f.endswith('.png') or f.endswith('.jpg')]
        if image_files:
            latest_image = max(image_files, key=lambda x: os.path.getctime(os.path.join(self.image_folder, x)))
            image_path = os.path.join(self.image_folder, latest_image)
            image = Image.open(image_path)
            photo = ImageTk.PhotoImage(image)

            self.image_label.configure(image=photo)
            self.image_label.image = photo

        self.root.after(1000, self.update_image)  # 每隔1秒检测一次

if __name__ == "__main__":
    root = tk.Tk()
    app = ImageDisplayApp(root, r"E:\360MoveData\Users\bai\Desktop\py\XXX")  # 替换为实际的图片文件夹路径
    root.mainloop()
