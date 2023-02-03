from PIL import Image, ImageDraw

im1 = Image.open('007.png').convert("RGBA")
width = im1.size[0]  # считываем ее ширину(длину)
height = im1.size[1]  # считываем ее высоту
if width > height:  # длина выше высоты
    image001_crop = im1.crop((0, 0, height, height))
else:
    image001_crop = im1.crop((0, 0, width, width))
image001_crop = image001_crop.resize((180, 180))  # по итогу у нас остается изображение с размерами 180 на 180

image001_crop.save('200.png', quality=100)
im1 = image001_crop

im2 = Image.open('layer3.png').convert("RGBA")

mask_im = Image.new("L", im1.size, 255)
draw = ImageDraw.Draw(mask_im)
draw.ellipse((7, 7, 169, 169), fill=0)
mask_im.save('mask_circle.jpg', quality=100)  # в режиме 95 много белых кругов, тогда как в режиме 100 нет белых кругов

im0 = Image.open('mask_circle.jpg').convert("L")


im1.paste(im0, (0,0), im0)
im1.save('dark6.png', quality=100)
img3 = Image.open('dark6.png')  # @cr333 https://stackoverflow.com/questions/765736/how-to-use-pil-to-make-all-white-pixels-transparent (изучить данный модуль, как он делает то что делает)
img3 = img3.convert("RGBA")
datas = img3.getdata()

newData = []
for item in datas:
    if item[0] == 255 and item[1] == 255 and item[2] == 255:
        newData.append((255, 255, 255, 0))
    else:
        newData.append(item)

img3.putdata(newData)
img3.save("ultra.png", "PNG")
img3.close()
im4 = Image.open('ultra.png').convert("RGBA")

im4.paste(im2, (0,0), im2)
im4.save('dark11.png', quality=100)


im1.close()
im2.close()
img3.close()
im4.close()
#mask_im.save('mask_circle.jpg', quality=95)