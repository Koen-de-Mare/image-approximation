import random
import math

from src.vector import Vector
from src.triangle import Triangle
from src.color import Color
from src.canvas import Canvas, black_canvas


class Genome:
    def __init__(self):
        self.triangles: list[Triangle] = []
        self.colors: list[Color] = []

    def mutate(self):
        assert (len(self.triangles) == len(self.colors))

        n: int = math.floor(random.random() * len(self.triangles))
        assert 0 <= n < len(self.triangles)

        a: float = random.random()
        b: float = random.random()
        c: float = random.random() * 0.6 - 0.3

        def clamp(x: float) -> float:
            return max(min(x, 1.0), 0.0)

        if a < 0.4:
            current_triangle = self.triangles[n]
            if b < 1 / 6:
                current_triangle.v1.x = clamp(current_triangle.v1.x + c)
            elif b < 2 / 6:
                current_triangle.v1.y = clamp(current_triangle.v1.y + c)
            elif b < 3 / 6:
                current_triangle.v2.x = clamp(current_triangle.v2.x + c)
            elif b < 4 / 6:
                current_triangle.v2.y = clamp(current_triangle.v2.y + c)
            elif b < 5 / 6:
                current_triangle.v3.x = clamp(current_triangle.v3.x + c)
            else:
                current_triangle.v3.y = clamp(current_triangle.v3.y + c)
            self.triangles[n] = current_triangle
        elif a < 0.9:
            current_color = self.colors[n]
            if b < 1 / 4:
                current_color.r = clamp(current_color.r + c)
            elif b < 2 / 4:
                current_color.g = clamp(current_color.g + c)
            elif b < 3 / 4:
                current_color.b = clamp(current_color.b + c)
            else:
                current_color.a = clamp(current_color.a + c)
            self.colors[n] = current_color
        else:
            n2: int = math.floor(b * len(self.triangles))
            temp_triangle = self.triangles[n]
            temp_color = self.colors[n]
            self.triangles[n] = self.triangles[n2]
            self.colors[n] = self.colors[n2]
            self.triangles[n2] = temp_triangle
            self.colors[n2] = temp_color

    def render(self, width: int, height: int) -> Canvas:
        assert (len(self.triangles) == len(self.colors))

        canvas: Canvas = black_canvas(width, height)
        for i in range(len(self.triangles)):
            canvas = render_triangle(self.triangles[i], self.colors[i], canvas)

        return canvas


def render_triangle(triangle: Triangle, color: Color, canvas: Canvas) -> Canvas:
    # find rectangle containing the considered triangle
    x_min: float = min(triangle.v1.x, triangle.v2.x, triangle.v3.x)
    x_max: float = max(triangle.v1.x, triangle.v2.x, triangle.v3.x)
    y_min: float = min(triangle.v1.y, triangle.v2.y, triangle.v3.y)
    y_max: float = max(triangle.v1.y, triangle.v2.y, triangle.v3.y)

    (px_min, py_min) = canvas.vector_to_index(Vector(x_min, y_min))
    (px_max, py_max) = canvas.vector_to_index(Vector(x_max, y_max))

    px_min: int = max(px_min, 0)
    px_max: int = min(px_max, canvas.width - 1)
    py_min: int = max(py_min, 0)
    py_max: int = min(py_max, canvas.height - 1)

    for px in range(px_min, px_max):
        for py in range(py_min, py_max):
            vector: Vector = canvas.index_to_vector(px, py)
            if triangle.contains(vector):
                canvas.draw(px, py, color)

    return canvas
