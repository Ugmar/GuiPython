from PIL import Image

def convert_color(r, g, b):
    return int(r * 0.4 + g * 0.4 + b * 0.2)

def bleach(file, path):
    img = Image.open(file).convert('RGB')
    width, height = img.size

    pixels = img.load()

    for x in range(width):
        for y in range(height):
            r, g, b = pixels[x, y]
            new_color = convert_color(r, g, b)
            pixels[x, y] = (new_color, new_color, new_color)


    img.save(path)
    img.close()

