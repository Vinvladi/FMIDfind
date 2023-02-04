from PIL import Image, ImageDraw
import png

width01 = 180
height01 = 180
image000 = Image.new(mode="RGBA", size=(width01, height01), color=(255, 255, 255))


image001 = Image.open('../../ver.1/001.png')  # считываем изображение 1 (основное)
width = image001.size[0]  # считываем ее ширину(длину)
height = image001.size[1]  # считываем ее высоту
if width > height:  # длина выше высоты
    image001_crop = image001.crop((0, 0, height, height))
else:
    image001_crop = image001.crop((0, 0, width, width))
image001_crop = image001_crop.resize((180, 180))  # по итогу у нас остается изображение с размерами 180 на 180

image001_crop.save('002.png', quality=100)

mask_im = Image.new("RGBA", image000.size, 0)
draw = ImageDraw.Draw(mask_im)
draw.ellipse((2, 2, 176, 176), fill=0)
mask_im.save('mask_circle.png', quality=100)

image000.paste(image001_crop, (0, 0), mask_im)
image000.save('gotovo.png', quality=100)

image000.close()
image001_crop.close()
mask_im.close()
