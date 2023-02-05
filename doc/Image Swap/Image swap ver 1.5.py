from PIL import Image, ImageDraw  # Включаем в программу 2 модуля Image и ImageDraw

# Переменные, которые участвуют в программе:
# input_image - начальное изображение открывает изображение 000.png
# input_image_crop - переменная после изменения crop (000a.png)
# layer_upper - верхний круг, на который мы будем накладывать свое изображение берется из (layer_upper.png)
# mask_ellipse_1 - создаем эллипс по координатам сравнение координат в (README.md в основной ветке), создается в L формате
# ellipse_good - готовый эллипс (круг)
# swap_image - это input_image уже в круге на белом фоне после итераций
# image_delete_white - удаление белых пикселей
# final_image - финальное значение

input_image = Image.open('000.png').convert("RGBA") # Работаем с базовым изображением, которое мы будем менять
width_input = input_image.size[0]  # считываем ее ширину(длину) (забабахать в def данный модуль)
height_input = input_image.size[1]  # считываем ее высоту
if width_input > height_input:  # длина выше высоты
    input_image_crop = input_image.crop((0, 0, height_input, height_input))
else:
    input_image_crop = input_image.crop((0, 0, width_input, width_input))
input_image_crop = input_image_crop.resize((180, 180))  # по итогу у нас остается изображение с размерами 180 на 180

input_image_crop.save('000a.png', quality=100) # (конец модуля) можно выход из функции def
swap_image = input_image_crop  # перебрасываю в новую переменную swap_image

layer_upper = Image.open('layer_upper.png').convert("RGBA")

mask_ellipse_1 = Image.new("L", swap_image.size, 255) # модуль создания овала L (причем использую 8-ми битную цветовую гамму), с 32 вроде нормально не робит, так как прозрачность не учитывается
draw = ImageDraw.Draw(mask_ellipse_1)
draw.ellipse((7, 7, 169, 169), fill=0)
mask_ellipse_1.save('mask_circle.jpg', quality=100)  # в режиме 95 много белых кругов, тогда как в режиме 100 нет белых кругов

ellipse_good = Image.open('mask_circle.jpg').convert("L") # замена переменной, скорей всего можно не конвертировать лишний раз


swap_image.paste(ellipse_good, (0,0), ellipse_good)
swap_image.save('000b.png', quality=100)  # input_image на данным моменте становится кругом сохранять в jpg
image_delete_white = Image.open('000b.png')  # @cr333 https://stackoverflow.com/questions/765736/how-to-use-pil-to-make-all-white-pixels-transparent (изучить данный модуль, как он делает то что делает)
image_delete_white = image_delete_white.convert("RGBA") # причем мы конвентрируем в 32-битное изображение возможно это не стоит делать
datas = image_delete_white.getdata()

newData = []
for item in datas:
    if item[0] == 255 and item[1] == 255 and item[2] == 255:
        newData.append((255, 255, 255, 0))
    else:
        newData.append(item)

image_delete_white.putdata(newData)
image_delete_white.save("ultra.png", "PNG")
image_delete_white.close()

final_image = Image.open('ultra.png').convert("RGBA")
final_image.paste(layer_upper, (0,0), layer_upper)
final_image.save('good.png', quality=100)


input_image.close()
layer_upper.close()
image_delete_white.close()
final_image.close()
#mask_ellipse_1.save('mask_circle.jpg', quality=95)