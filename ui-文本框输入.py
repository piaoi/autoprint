# 将Entry设置成只读
# 有些信息我们输入完成确定后，就不希望它再被修改了，这时候我们可以设置他的state属性，设置为可读

import tkinter as tk

window = tk.Tk()

entry_var = tk.StringVar()
entry = tk.Entry(window,width=20,textvariable=entry_var)
entry.pack()
entry_var.set('在此输入')

def change_state():
    entry.configure(state='readonly')
    var = entry.get()		# 调用get()方法，将Entry中的内容获取出来
    print(var)
    # 我们可以用控件的configure方法修改控件的属性，设置控件状态的属性就是state
button = tk.Button(window,text='单击',command=change_state).pack()
window.mainloop()
