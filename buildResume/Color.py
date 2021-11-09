RED = [255, 0, 0]
GREEN = [0, 255, 0]
BLUE = [0, 0, 255]
BLACK = [0, 0, 0]
GREY = [.45, .45, .45]


def set_color(pdf, rgb):
    pdf.setFillColorRGB(rgb[0], rgb[1], rgb[2])
