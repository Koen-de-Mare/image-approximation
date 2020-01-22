import sys
from typing import Tuple

from PIL import Image
from PIL import ImageDraw

from src.color import *
from src.vector import Vector


class Canvas:
    def __init__(self):
        self.width: int = 0
        self.height: int = 0
        self.pixels: list[Color] = []

    def draw(self, px: int, py: int, brush_color: Color):
        assert(px >= 0)
        assert(py >= 0)
        assert(px < self.width)
        assert(py < self.height)

        # remember that this is not a copy, but merely a reference.
        # code should still behave fine though
        current_color: Color = self.pixels[px][py]
        new_color: Color = stack_colors(brush_color, current_color)
        self.pixels[px][py]: Color = new_color


    def vector_to_index(self, vector: Vector) -> Tuple[int, int]:
        px = math.floor(vector.x * self.width)
        py = math.floor(vector.y * self.height)

        return (px, py)

    def index_to_vector(self, px: int, py: int) -> Vector:
        result = Vector()
        result.x = px / self.width
        result.y = py / self.height
        return result

def black_canvas(width: int, height: int) -> Canvas:
    assert (width > 0)
    assert (height > 0)

    canvas = Canvas()

    canvas.width: int = width
    canvas.height: int = height

    canvas.pixels: list[Color] = [[black() for y in range(height)] for x in range(width)]

    return canvas

def import_image(filename: str) -> Canvas:
    image = Image.open(filename)
    #print(im.format, im.size, im.mode)

    (width, height) = image.size

    canvas = black_canvas(width, height)

    for px in range(width):
        for py in range(height):
            im_color = image.getpixel((px, py))
            color = from_pil(im_color)
            canvas[px][py] = color

    return canvas


def export_image(canvas: Canvas, filename: str):
    image = Image.new("RGB", (canvas.width, canvas.height))

    draw = ImageDraw.Draw(image)
    for px in range(canvas.width):
        for py in range(canvas.height):
            canvas_color: Color = canvas.pixels[px][py]
            pil_color = canvas_color.to_pil()
            draw.point([(px,py)], pil_color)

    image.save("output/" + filename + ".png")