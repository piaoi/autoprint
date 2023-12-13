
import tkinter as tk
import sys

class ConsoleRedirector:
    def __init__(self, text_widget):
        self.text_widget = text_widget

    def write(self, message):
        self.text_widget.insert(tk.END, message)

def main():
    root = tk.Tk()
    root.title("Console Output")

    text = tk.Text(root,width= 50 ,height= 10)
    text.pack()

    sys.stdout = ConsoleRedirector(text)

    print("Hello, this message will be redirected to the text widget")
    # 示例:计数器v3
    print("请输入一个整数！序列号不为字符2！")

    root.mainloop()

if __name__ == "__main__":
    main()


