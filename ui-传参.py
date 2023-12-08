
from gc import enable
from tkinter import *
import logging


class Window:
    def __init__(self):
        self.window = Tk()
        self.window.title('演示写入数据')

        # 获取屏幕大小
        screenwidth = self.window.winfo_screenwidth()  # 屏幕宽
        screenheight = self.window.winfo_screenheight()  # 屏幕高

        # 窗口居中
        size = self.window_of_center(screenwidth, screenheight)
        self.window.geometry(size)
        self.window.resizable(0, 0)  # 禁止调整大小

        # 输入的数据
        self.message = StringVar()

        # 页面布局
        self.layout()
        self.window.mainloop()

    @staticmethod
    def window_of_center(screenwidth, screenheight, width=400, height=200):
        """
        设置窗口居中
        :param screenwidth: 屏幕宽
        :param screenheight: 屏幕高
        :param width: 窗体宽
        :param height: 窗体高
        :return: 窗体大小及位置 size
        """
        # 设置窗口在屏幕中间
        size = '%dx%d+%d+%d' % (width,
                                height,
                                (screenwidth - width) / 2,
                                (screenheight - height) / 2)

        logging.info(f'屏幕(宽 x 高): {screenwidth} x {screenheight}')
        logging.info(f'窗口(宽 x 高): {width} x {height}')

        return size

    def layout(self):
        """
        页面布局
        :return:
        """
        # 标签
        hint = Label(self.window, text='请输入:', fg='blue', font=('宋体', 10), anchor='e')
        entry = Entry(self.window, bd=1, textvariable=self.message)
        btn = Button(self.window, text='确定', command=lambda: self.show_text(text))
        text = Text(self.window, width=45, height=10)

        # 布局
        hint.place(x=5, y=10, width=80, height=20)
        entry.place(x=95, y=10, width=200, height=20)
        btn.place(x=300, y=10, height=20)
        text.place(x=40, y=50,width=300, height=100)  #显示的地方
        

    def show_text(self, text):
        """
        插入文本内容，带参数
        :param text: 文本框
        :return:
        """
        # 写入 text
        text.config(state=NORMAL)  # 解除封印：设置Text文本框为 “不能编辑”
        text.insert(INSERT, self.message.get())
        logging.info(f'写入 message = {self.message.get()}')
        

        # 清空
        self.message.set('')
        logging.info('清空 message 成功')
        text.config(state=DISABLED)  # 设置Text文本框为 “不能编辑”


if __name__ == '__main__':
    # 设置日志等级
    logger = logging.getLogger()
    logger.setLevel(logging.INFO)

    # 调用窗体
    Window()
