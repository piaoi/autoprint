import win32ui
import win32con
import win32print
from PIL import Image, ImageWin

# 获取默认打印机
printer_name = win32print.GetDefaultPrinter()

# 创建打印设备上下文（DC）
hprinter = win32print.OpenPrinter(printer_name)
printer_info = win32print.GetPrinter(hprinter, 2)
dc = win32ui.CreateDC()
dc.CreatePrinterDC(printer_name)

# 设置打印纸尺寸（57*20mm）
dc.SetMapMode(win32con.MM_TWIPS)
dc.SetViewportOrg((0, 0))
dc.SetWindowExt((57*1440, 20*1440))  # 1mm = 1440 twips

# 开始打印
dc.StartDoc('Combined Document')
dc.StartPage()

# 打印文本
text_to_print = "Hello, World!"
dc.TextOut(100, 100, text_to_print)

# 打印图片
image_path = "--100.png"
bmp = Image.open(image_path)
scaled_width, scaled_height = 10*1440, 10*1440  # 10mm * 1440 twips/mm
bmp = bmp.resize((int(scaled_width/1440), int(scaled_height/1440)))  # Resize image to 10mm*10mm
dib = ImageWin.Dib(bmp)
dib.draw(dc.GetHandleOutput(), (100, 200, 100+scaled_width, 200+scaled_height))

# 结束打印
dc.EndPage()
dc.EndDoc()
dc.DeleteDC()
