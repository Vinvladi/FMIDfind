from PIL import Image, ImageDraw, ImageFont

for a in range(2000350001,2000500001,1):
    name = str(a) + str('.jpg')
    img = Image.new('L', (180, 180), 'black') # 24 bit color - RGB / RGBA / L / 1
    font = ImageFont.truetype("arial.ttf", size=36)
    idraw = ImageDraw.Draw(img)
    idraw.text((40, 20), name[0:4], font=font, fill=255) # fill - параметр отвечающий за цвет, fill = 0 - черный / 255 - белый
    idraw.text((40, 70), name[4:7], font=font, fill=255)
    idraw.text((40, 120), name[7:10], font=font, fill=255)
    img.save(name)

'''
StaffFind 2000350000 2000500000
StaffFind 2000500001 2000700000
StaffFind 2000700001 2000900000
StaffFind 2000900001 2001000000
StaffFind 2001000001 2001200000
'''



#StaffFind 2002000001 2002200001
#StaffFind 2002200001 2002400001
#StaffFind 2002400001 2002600001
#StaffFind 2002600001 2002800001
#StaffFind 2002800001 2003000001
#StaffFind 2003000001 2003200001
#StaffFind 2003200001 2003400001
#StaffFind 2003400001 2003600001