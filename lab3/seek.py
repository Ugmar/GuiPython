from PIL import Image
from math import log10

# Коды ошибки
ERROR_NOT_HIDE_STRING = 1
ERROR_INVALID_FORMAT = 2

# Получение 1 бита
def get_bit(color):
    return bin(color)[-1]

# Обработка компонентов пикселя
def processing_pixel(pixel, current):
    for color in pixel:
        current += get_bit(color)

    return current

# Основная функция расшифровки
def img_to_string(file):
    # Проверка формата
    form = file.split('.')[1]
    if form.lower() != 'bmp':
        return ERROR_INVALID_FORMAT

    # Открытие изображения
    img = Image.open(file).convert("RGB")
    width, height = img.size

    # Флаг, отображающий нашлась ли вся длина строки
    full_len = False
    # Изначальная длина
    lenght = 1
    # Текущий символ
    current = ''
    # Набранная строка
    string = ''
    x = 0
    y = 0

    pixels = img.load()

    while x < width and lenght > 0:
        while y < height and lenght > 0:
            pixel = pixels[x, y]
            # "Собирание" битов символа
            current = processing_pixel(pixel, current)
            if len(current) == 9:
                # Получение символа
                ascii_symbol = chr(int(current[:8], 2))
                if not full_len:
                    # Обновление длины строки
                    if ascii_symbol.isdigit():
                        lenght *= 10
                        lenght += int(ascii_symbol)
                    else:
                        # Проверка, на существование сокрытой строки
                        if lenght == 1:
                            return ERROR_NOT_HIDE_STRING
                        string += ascii_symbol
                        lenght %= 10 ** int(log10(lenght))
                        lenght -= 1
                        full_len = True
                else:
                    # Обновление строки
                    string += ascii_symbol
                    lenght -= 1
                current = ''
            y += 1
        x += 1
    return string
