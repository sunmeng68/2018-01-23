# -*- coding: utf-8 -*-
from PIL import Image,ImageFilter,ImageDraw,ImageFont
import random

#操作图像
im =Image.open('C:\\Users\Sun\Desktop\cat.jpg')
w,h=im.size
print ('Original image size:%sx%s'%(w,h))
im.thumbnail((w//2,h//2))
print ('Resize image size : %sx%s'%(w//2,h//2))
#缩放后的图像保存
#im.save('C:\\Users\Sun\Desktop\cat2.jpg','jpeg')

#给图像增加模糊效果
pic=Image.open('C:\\Users\Sun\Desktop\cat.jpg')
pic2=pic.filter(ImageFilter.BLUR)
pic2.save('blurcat.jpg','jpeg')


#PIL的ImageDraw提供了一系列绘图方法，让我们可以直接绘图。比如要生成字母验证码图片：
#随机字母
def rndChar():
    return chr(random.randint(65,90))
#随机颜色
def rndColor():
    return (random.randint(64,255),random.randint(64,255),random.randint(64,255))
#随机颜色2
def rndColor2():
    return (random.randint(32,127),random.randint(32,127),random.randint(32,127))
#验证码大小
width =60*5
height=60
image=Image.new('RGB',(width,height),(255,255,255))
#创建font对象
font=ImageFont.truetype('arial.ttf',36)
#创建draw对象
draw=ImageDraw.Draw(image)
#填充每个对象
for x in range(width):
    for y in range(height):
        draw.point((x,y),fill=rndColor())
#生成随机字
for t in range(5):
    draw.text((60*t+10,10),rndChar(),font=font,fill=rndColor2())
#对文字进行模糊
image=image.filter(ImageFilter.BLUR)
#对文字进行旋转

image.save('验证码.jpg','jpeg')

