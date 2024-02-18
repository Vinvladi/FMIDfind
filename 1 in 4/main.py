from PIL import Image

# Открываем изображение
img = Image.open("0000.png")

# Получаем размеры изображения
width, height = img.size

# Разделяем изображение на 4 части
part1 = img.crop((0, 0, width//2, height//2))
part2 = img.crop((width//2, 0, width, height//2))
part3 = img.crop((0, height//2, width//2, height))
part4 = img.crop((width//2, height//2, width, height))

# Сохраняем каждую часть в отдельный файл
part1.save("part1.png")
part2.save("part2.png")
part3.save("part3.png")
part4.save("part4.png")