
# import tkinter as tk

# class AutoScrollApp:
#     def __init__(self, root):
#         self.root = root
#         self.root.title("Auto Scroll")

#         self.scrollbar = tk.Scrollbar(self.root)
#         self.scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

#         self.text = tk.Text(self.root, yscrollcommand=self.scrollbar.set)
#         self.text.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

#         self.scrollbar.config(command=self.text.yview)

#         self.text.bind("<Key>", self.scroll_to_end)

#     def scroll_to_end(self, event):
#         self.text.see(tk.END)

# if __name__ == "__main__":
#     root = tk.Tk()
#     app = AutoScrollApp(root)
#     root.mainloop()

import tkinter as tk

def scroll_to_bottom():
    text_box.yview(tk.END)

root = tk.Tk()

scrollbar = tk.Scrollbar(root)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

text_box = tk.Text(root, yscrollcommand=scrollbar.set)
text_box.pack(side=tk.LEFT, fill=tk.BOTH)

scrollbar.config(command=text_box.yview)

# 模拟数据输入
for i in range(1, 100):
    text_box.insert(tk.END, f"这是第 {i} 行\n")
    # 每插入一行文本后，将文本框滚动到底部
    scroll_to_bottom()

root.mainloop()