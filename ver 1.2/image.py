from PIL import Image, ImageDraw, ImageFont

for a in range(2002000001,2002200001,1):
    name = str(a) + str('.jpg')
    img = Image.new('RGB', (180, 180), 'black')
    font = ImageFont.truetype("arial.ttf", size=36)
    idraw = ImageDraw.Draw(img)
    idraw.text((40, 20), name[0:4], font=font)
    idraw.text((40, 70), name[4:7], font=font)
    idraw.text((40, 120), name[7:10], font=font)
    img.save(name)


#StaffFind 2002000001 2002200001
#StaffFind 2002200001 2002400001
#StaffFind 2002400001 2002600001
#StaffFind 2002600001 2002800001
#StaffFind 2002800001 2003000001
#StaffFind 2003000001 2003200001
#StaffFind 2003200001 2003400001
#StaffFind 2003400001 2003600001