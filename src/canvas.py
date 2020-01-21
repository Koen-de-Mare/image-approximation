import math

from src.color import *
from src.vector import Vector


class Canvas:
    def __init__(self, width: int, height: int):
        assert(width > 0)
        assert(height > 0)

        self.width = width
        self.height = height

        self.pixels = [[black() for y in range(height)] for x in range(width)]

    def draw(self, px: int, py: int, brush_color: Color):
        assert(px >= 0)
        assert(py >= 0)
        assert(px < self.width)
        assert(py < self.height)

        # remember that this is not a copy, but merely a reference.
        # code should still behave fine though
        current_color = self.pixels[px][py]
        new_color = stack_colors(brush_color, current_color)
        self.pixels[px][py] = new_color


    def vector_to_index(self, vector: Vector) -> tuple[int, int]:
        px = math.floor(vector.x * self.width)
        py = math.floor(vector.y * self.height)

        return (px, py)

    def index_to_vector(self, px: int, py: int) -> Vector:
        result = Vector()
        result.x = px / self.width
        result.y = py / self.height
        return result
