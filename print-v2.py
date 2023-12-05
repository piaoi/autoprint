import win32ui
import win32print
from PIL import Image, ImageWin

# 打印文本
def print_text(text):
    printer_name = win32print.GetDefaultPrinter()
    hprinter = win32print.OpenPrinter(printer_name)
    printer_info = win32print.GetPrinter(hprinter, 2)
    dc = win32ui.CreateDC()
    dc.CreatePrinterDC(printer_name)
    dc.StartDoc('Text Document')
    dc.StartPage()
    dc.TextOut(10, 10, text)
    dc.EndPage()
    dc.EndDoc()
    dc.DeleteDC()

# 打印图片
def print_image(image_path):
    printer_name = win32print.GetDefaultPrinter()
    hprinter = win32print.OpenPrinter(printer_name)
    printer_info = win32print.GetPrinter(hprinter, 2)
    dc = win32ui.CreateDC()
    dc.CreatePrinterDC(printer_name)
    dc.StartDoc('Image Document')
    dc.StartPage()
    bmp = Image.open(image_path)
    dib = ImageWin.Dib(bmp)
    dib.draw(dc.GetHandleOutput(), (10, 10, 10+bmp.width, 10+bmp.height))
    dc.EndPage()
    dc.EndDoc()
    dc.DeleteDC()

# 打印文本和图片
text_to_print = "Hello, World!"
image_to_print = "--100.png"

print_text(text_to_print)
print_image(image_to_print)
