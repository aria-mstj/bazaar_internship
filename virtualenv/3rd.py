from PIL import Image


def create_image(i, j):
    pic = Image.new("RGB", (i, j), "white")
    return pic


def get_pixel(pic, i, j):
    # Inside image bounds?
    width, height = pic.size
    if i > width or j > height:
        return None

    pixel = pic.getpixel((i, j))
    return pixel


image = create_image(1000, 1000)
pixels = image.load()
for i in range(0, 1000, 1):
    for j in range(0, 1000):
        if i % 50 < 25:
            pixels[i, j] = (100, 10, 10)
        else:
            pixels[i, j] = (10, 10, 100)

image.show()
