from PIL import Image, ImageDraw
from pathlib import Path

im = Image.open('001.png') #считываем изображение 1
width = im.size[0]
height = im.size[1]
if width > height:
    im_crop = im.crop((0, 0, height, height))
else:
    im_crop = im.crop((0, 0, width, width))

im_crop = im_crop.resize((180, 180))

layerw = Image.open("layer3.png")
img = img.convert("RGBA")

im_crop.save('002.jpg', quality=100)



img.putdata(newData)
img.save("mod_img1.png", "PNG")


im1 = Image.open('fon.jpg')
im2 = Image.open('guido-van-rossum.jpg')

im1.paste(im2)
im1.save('fon_pillow_paste.jpg', quality=95)

im1.close()
im2.close()
