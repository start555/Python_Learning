# Задание по Pillow:
# Программа создает картинку c разрешением FullHD и рисует слева направо вертикальные линии шириной 1 px.
# Цвет первой линии (128, 128, 128). Цвет каждой последующей имеет случайный сдвиг по каждой из координат цвета на (+-10).
# Например (125, 135, 120), следующий цвет определяется относительно предыдущего.
# При этом следите за диапазоном. Если больше 255, то равен 255, если меньше 0, то равен 0.

from PIL import Image, ImageDraw
import random


im = Image.new('RGB', (1920, 1080))
draw = ImageDraw.Draw(im)
cd1 = 128
cd2 = 128
cd3 = 128
for i in range(0, im.size[0]):
    cda = random.randrange(-10, 10)
    cd1 += cda
    if cd1 > 255:
        cd1 = 255
    elif cd1 < 0:
        cd1 = 0

    cdb = random.randrange(-10, 10)
    cd2 += cdb
    if cd2 > 255:
        cd2 = 255
    elif cd2 < 0:
        cd2 = 0

    cdc = random.randrange(-10, 10)
    cd3 += cdc
    if cd3 > 255:
        cd3 = 255
    elif cd3 < 0:
        cd3 = 0

    draw.line((0+i, 0, 0+i, im.size[0]), fill=(cd1, cd2, cd3), width=1)
    i += 1
im.save('psihodel.jpg')
im.show()


