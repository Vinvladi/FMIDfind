from PIL import Image, ImageDraw

im1 = Image.open('../../ver 1.2/002.png').convert("RGBA")
im2 = Image.open('../../ver 1.2/layer3.png').convert("RGBA")

mask_im = Image.new("L", im1.size, 255)
draw = ImageDraw.Draw(mask_im)
draw.ellipse((5, 5, 173, 173), fill=0)
mask_im.save('mask_circle.jpg', quality=100) # в режиме 95 много белых кругов, тогда как в режиме 100 нет белых кругов

im0 = Image.open('../../ver 1.2/mask_circle.jpg').convert("L")

im1.paste(im0, (0,0), im0)
im1.save('dark6.png', quality=100)
im1.paste(im2, (0,0), im2)
im1.save('dark.png', quality=100)

img3 = Image.open('../../ver 1.2/dark.png')  # @cr333 https://stackoverflow.com/questions/765736/how-to-use-pil-to-make-all-white-pixels-transparent (изучить данный модуль, как он делает то что делает)
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

im1.close()
im2.close()
img3.close()
#mask_im.save('mask_circle.jpg', quality=95)