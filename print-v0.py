import win32print
import win32ui
from PIL import Image, ImageWin

# 列出所有打印机
printers = [printer[2] for printer in win32print.EnumPrinters(2)]
for i, printer in enumerate(printers):
    print(f"{i+1}: {printer}")

# 选择打印机
choice = int(input("选择要使用的打印机 (输入对应的序号): ")) - 1
printer_name = printers[choice]

# 加载图片
image_path = r"--100.png"
image = Image.open(image_path)

# 创建设备描述表
hDC = win32ui.CreateDC()
hDC.CreatePrinterDC(printer_name)

# 开始文档
hDC.StartDoc(image_path)

# 开始页面
hDC.StartPage()

# 绘制位图
dib = ImageWin.Dib(image)
dib.draw(hDC.GetHandleOutput(), (0, 0, image.width, image.height))

# 结束页面
hDC.EndPage()

# 结束文档
hDC.EndDoc()

# 删除设备描述表对象
del hDC

print("打印成功！")

