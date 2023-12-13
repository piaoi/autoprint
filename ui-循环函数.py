#函数一，垃圾
# import tkinter as tk
# from tkinter import messagebox
# import time
# from watchdog.observers import Observer
# from watchdog.events import FileSystemEventHandler

# class FileChangeHandler(FileSystemEventHandler):
#     def __init__(self, filename):
#         self.filename = filename

#     def on_modified(self, event):
#         if not event.is_directory and event.src_path == self.filename:
#             # 文件被修改时的处理逻辑
#             with open(self.filename, 'r') as file:
#                 lines = file.readlines()
#                 if lines:
#                     last_line = lines[-1].strip()
#                     print(last_line)
#                     messagebox.showinfo("文件内容变化", last_line)

# def start_file_monitoring(filename):
#     event_handler = FileChangeHandler(filename)
#     observer = Observer()
#     observer.schedule(event_handler, path='.', recursive=False)
#     observer.start()

#     root = tk.Tk()
#     root.withdraw()

#     try:
#         while True:
#             time.sleep(1)
#     except KeyboardInterrupt:
#         observer.stop()
#     observer.join()

# if __name__ == '__main__':
#     filename = 'file.txt'  # 要监听的文件名
#     start_file_monitoring(filename)




#函数二，可行
import tkinter as tk

def update_label():
    # 更新标签内容
    global counta
    counta += 1
    label.config(text="Count: {}".format(counta))

    # 继续定时更新
    label.after(1000, update_label)  # 设置更新的间隔时间（以毫秒为单位，这里是1秒）

# 创建窗口
window = tk.Tk()

# 创建标签
label = tk.Label(window, text="Count: 0")
label.pack()

# 定时更新标签内容
counta = 0
update_label()

# 启动窗口的事件循环
window.mainloop()



#函数三 
# import tkinter as tk

# def long_running_task():
#     # 模拟一个耗时操作
#     import time
#     time.sleep(5)
#     print("Long running task finished!")

# def button_click():
#     print("Button clicked!")
#     window.after(0, long_running_task)

# window = tk.Tk()

# button = tk.Button(window, text="Click Me", command=button_click)
# button.pack()

# window.mainloop()

#函数四
# import tkinter as tk
 
# master = tk.Tk()
 
# def my_mainloop():
#     print ("Hello World!")
#     master.after(1000, my_mainloop)    
 
# master.after(1000, my_mainloop)
 
# master.mainloop()

