# from tkinter import *

# def update_label():
#     console_info = "aaaaa" + '\n' + "aa123"  # 这里替换为你要实时输出的控制台信息
#     label.config(text=console_info)
#     root.after(1000, update_label)  # 每隔1秒更新一次Label的内容

# root = Tk()
# root.geometry("500x200")

# label = Label(root, text="", font=("Arial", 14))
# label.pack()
# label.config(width=50, height=20)
# label.config(background='red')

# update_label()

# root.mainloop()
import sys
import tkinter as tk

class StdoutRedirector(object):
    def __init__ (self, text_widget):
        self.text_widget = text_widget
    def write(self, str):
        self.text_widget.insert(tk.END,str)
        self.text_widget.see(tk.END)
root = tk.Tk()
text = tk.Text(root)
text .pack()
#重定向标准输出
sys.stdout = StdoutRedirector(text)
print("Hello，world!") # 新出将会显示在文本框中
root.mainloop()