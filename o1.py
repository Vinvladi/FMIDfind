name = str(a) + str('.jpg')
img = Image.new('RGB', (180, 180), 'black')
font = ImageFont.truetype("arial.ttf", size=36)
idraw = ImageDraw.Draw(img)
idraw.text((40, 20), name[0:4], font=font)
idraw.text((40, 70), name[4:7], font=font)
idraw.text((40, 120), name[7:10], font=font)
img.save(name)

background = Image.open("check00001.png")
foreground = Image.open("check00002.png")

background.paste(foreground, (0, 0), foreground)
background.show()