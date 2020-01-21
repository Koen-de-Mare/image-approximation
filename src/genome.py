import math

from src.canvas import Canvas
from src.vector import Vector
from src.triangle import Triangle
from src.color import Color
from src.canvas import Canvas

class Genome:
    def __init__(self):
        self.triangles = []
        self.colors = []

    def render(self, width: int, height: int):
        assert(self.triangles.len() == self.colors.len())

        canvas = Canvas(width, height)

        #for i in range(0, )
        #TODO


def render_triangle(triangle: Triangle, color: Color, canvas: Canvas) -> Canvas:
    # find rectangle containing the considered triangle
    x_min = min(triangle.v1.x, triangle.v2.x, triangle.v3.x)
    x_max = max(triangle.v1.x, triangle.v2.x, triangle.v3.x)
    y_min = min(triangle.v1.y, triangle.v2.y, triangle.v3.y)
    y_max = max(triangle.v1.y, triangle.v2.y, triangle.v3.y)

    (px_min, py_min) = canvas.vector_to_index(Vector(x_min, y_min))
    (px_max, py_max) = canvas.vector_to_index(Vector(x_max, y_max))

    px_min = max(px_min, 0)
    px_max = min(px_max, canvas.width - 1)
    py_min = max(py_min, 0)
    py_max = min(py_max, canvas.height - 1)

    for px in range(px_min, px_max):
        for py in range(py_min, py_max):
            vector = canvas.index_to_vector(px, py)
            if triangle.contains(vector):
                canvas.draw(px, py, color)
