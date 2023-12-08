import tkinter as tk
import sys
 
def redirect_stdout_to_tkinter(text_widget):
    class StdoutRedirector:
        def __init__(self, text_widget):
            self.text_widget = text_widget
 
        def write(self, message):
            self.text_widget.insert('end', message)
            self.text_widget.see('end')
 
    sys.stdout = StdoutRedirector(text_widget)
 
# 创建Tkinter窗口
window = tk.Tk()
 
# 创建文本框用于显示输出
output_text = tk.Text(window)
output_text.pack()
 
# 重定向标准输出到文本框
redirect_stdout_to_tkinter(output_text)
 
# 执行print语句，输出将显示在文本框中
print("Hello, Tkinter!")
 
# 运行Tkinter主循环
window.mainloop()
