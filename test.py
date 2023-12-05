from PIL import Image, ImageDraw, ImageFont
import qrcode
import win32print

def comb(png1, png2, style='horizontal'):

    img1, img2 = Image.open(png1), Image.open(png2)
    # 统一图片尺寸，可以自定义设置（宽，高）
    img1 = img1.resize((200, 200), Image.ANTIALIAS)
    img2 = img2.resize((370, 200), Image.ANTIALIAS)
    size1, size2 = img1.size, img2.size
    if style == 'horizontal':
        joint = Image.new('RGB', (size1[0] + size2[0], size1[1]))
        loc1, loc2 = (0, 0), (size1[0], 0)
        joint.paste(img1, loc1)
        joint.paste(img2, loc2)
        joint.save('putout.png')
    elif style == 'vertical':
        joint = Image.new('RGB', (size1[0], size1[1] + size2[1]))
        loc1, loc2 = (0, 0), (0, size1[1])
        joint.paste(img1, loc1)
        joint.paste(img2, loc2)
        joint.save('putout1.png')

if __name__ == '__main__':
    # 两张图片地址：
    png1 = r"./--100.png"
    png2 = r"./99999.png"
    # 左右拼接
    comb(png1, png2, style='horizontal')

    # 上下拼接
    # comb(png1, png2, style='vertical')
    
# 打开图片
image = Image.open('putout.png')

# 在右侧添加文字
draw = ImageDraw.Draw(image)
text = "Your text here"
font = ImageFont.truetype('arial.ttf', 20)  # 修改字体和大小
text_width, text_height = draw.textsize(text, font)
x = image.width - text_width - 220  # 文字位置，可以自行调整
y = image.height // 2 - text_height // 2
draw.text((x, y), text, font=font, fill='black')

# 显示图片
image.show()

# 保存图片
image.save('final.png')

# 使用打印机打印图片
printer_name = win32print.GetDefaultPrinter()
win32print.SetDefaultPrinter(printer_name)
win32print.PrintFile(printer_name, 'final.png', "Printing with Python")