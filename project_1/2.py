from PIL import Image

# Открываем изображение
image = Image.open('1.png')

# Конвертируем изображение в режим работы с пикселями
image = image.convert('RGBA')

# Получаем данные пикселей
pixels = image.load()

# Удаляем конкретные пиксели
pixels_to_remove = [(0, 0), (1, 1), (1, 2)]
for pixel in pixels_to_remove:
    pixels[pixel[0], pixel[1]] = (0, 0, 0, 0)  # Задаем черный прозрачный пиксель

# Сохраняем измененное изображение
image.save('modified_image.png')