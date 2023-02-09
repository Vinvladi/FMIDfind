from PIL import Image, ImageDraw

input_image = Image.open('001.jpg').convert("RGBA")
input_image.save('000.png', quality=100)