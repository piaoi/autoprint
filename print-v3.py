from PIL import Image, ImageDraw, ImageFont,ImageWin
import qrcode
import win32print
import win32ui
import time
import datetime

date = time.strftime("%Y-%m-%d %H:%M:%S")

def comb(png1, png2, style='horizontal'):

    img1, img2 = Image.open(png1), Image.open(png2)
    # 统一图片尺寸，可以自定义设置（宽，高）
    img1 = img1.resize((550, 200), Image.ANTIALIAS) #以第一张图片高度为准
    img2 = img2.resize((100, 100), Image.ANTIALIAS)
    size1, size2 = img1.size, img2.size
    if style == 'horizontal':
        joint = Image.new('RGB', (size1[0] + size2[0], size1[1]))
        loc1, loc2 = (100, 0), (0, 50)
        joint.paste(img1, loc1)
        joint.paste(img2, loc2)
        joint.save('putout.png')
    elif style == 'vertical':
        joint = Image.new('RGB', (size1[0], size1[1] + size2[1]))
        loc1, loc2 = (100, 0), (50,0)
        joint.paste(img1, loc1)
        joint.paste(img2, loc2)
        joint.save('putout1.png')

if __name__ == '__main__':
    # 两张图片地址：
    png1 = r"./99999.png"
    png2 = r"./--100.png"
    # 左右拼接
    comb(png1, png2, style='horizontal')

    # 上下拼接
    # comb(png1, png2, style='vertical')
    
# 打开图片
image = Image.open('putout.png')

# 在右侧添加文字
draw = ImageDraw.Draw(image)
text = "No." + date
font = ImageFont.truetype('arial.ttf', 30)  # 修改字体和大小
text_width, text_height = draw.textsize(text, font)
x = image.width - text_width - 230  # 文字位置，可以自行调整
y = image.height // 2 - text_height // 2
draw.text((x, y), text, font=font, fill='black')
# draw.text((x, y), text, font=font, fill='white')


# 显示图片
image.show()

# 保存图片
image.save('final.png')



# 使用打印机打印图片
# 列出所有打印机
# printers = [printer[2] for printer in win32print.EnumPrinters(2)]
# for i, printer in enumerate(printers):
#     print(f"{i+1}: {printer}")

# 选择打印机
# choice = int(input("选择要使用的打印机 (输入对应的序号): ")) - 1
# printer_name = printers[choice]

# 获取默认打印机
printer_name = win32print.GetDefaultPrinter()


# 加载图片
image_path = r"final.png"
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