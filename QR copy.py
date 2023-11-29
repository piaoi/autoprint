import qrcode
 
with open("output.txt", "r") as read_file:  #也为了方便注释写的清楚一些吧，这是打开当前目录下的一个txt文件。就是要生成二维码的网址
    # file = open('E:\\360MoveData\\Users\\bai\\Desktop\\py\\test.txt', encoding='gbk')  #绝对路径

    for line in read_file.readlines():
        line = line.strip('\n')  #去掉列表中每一个元素的换行符
        
        qr = qrcode.QRCode(
    	version=2,
    	error_correction=qrcode.constants.ERROR_CORRECT_L,
    	box_size=10,
    	border=1
        )#设置二维码的大小
        qr.add_data(line)
        qr.make(fit=True)
        img = qr.make_image()
        line2=line[-3:]#取后几位命名
        print(line2)
        img.save(line2+".png")
        
        print(line)