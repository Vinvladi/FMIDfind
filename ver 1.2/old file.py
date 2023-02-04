from PIL import Image

im1 = Image.open('002.png')
im2 = Image.open('layer3.png')

im1.paste(im2)
im1.save('dark.png', quality=80)

im1.close()
im2.close()