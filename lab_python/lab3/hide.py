from PIL import Image

# Коды ошибок
ERROR_LEN_STRING = 1
ERROR_INVALID_FORMAT = 2
ERROR_INVALID_FIRST_EL = 3
OK = 0

# Заменяем бит для каждого цвета пикселя
def update_pixel(r, g, b, bin_char):
    r = (r & (~0b1)) | int(bin_char[0])
    g = (g & (~0b1)) | int(bin_char[1])
    if len(bin_char) >= 3:
        b = (b & (~0b1)) | int(bin_char[2])
        bin_char = bin_char[3:]
    else:
        bin_char = bin_char[2:]
    return r, g, b, bin_char

# Получение текущего символа
def get_bin_char(string):
    bin_char = bin(ord(string[0]))[2:].zfill(8)
    string = string[1:]
    return bin_char, string

# Основная функция сокрытия
def string_to_img(string, name_img, path):
    # Первый символ не может быть числом
    if string[0].isdigit():
        return ERROR_INVALID_FIRST_EL

    # Проверка формата
    name, form = name_img.split('.')
    if form.lower() != 'bmp':
        return ERROR_INVALID_FORMAT

    # Открытие изображения
    img = Image.open(name_img).convert("RGB")
    width, height = img.size

    # Добавление в начало строки ее длину
    string = str(len(string)) + string

    # Проверка возможности зашифровать строку
    if len(string * 3) > width * height:
        return ERROR_LEN_STRING

    # Список всех пикселей
    pixels = img.load()

    # Первый символ
    bin_char, string = get_bin_char(string)
    x, y = 0, 0
    while x < width and bin_char:
        while y < height and bin_char:
            # Текущий пиксель
            pixel = pixels[x, y]
            r, g, b = pixel
            # изменяем компоненты пикселя
            r, g, b, bin_char = update_pixel(r, g, b, bin_char)
            pixels[x, y] = (r, g, b)

            # Обновление символа
            if not bin_char:
                if string:
                    bin_char, string = get_bin_char(string)
            y += 1
        x += 1

    # сохранение нового изображения
    img.save(path)
    return OK
