from src.color import *
from src.vector import Vector
from src.triangle import Triangle
from src.canvas import *
from src.genome import render_triangle

triangle = Triangle()
triangle.v1.x = 0.1
triangle.v1.y = 0.1
triangle.v2.x = 0.9
triangle.v2.y = 0.1
triangle.v3.x = 0.1
triangle.v3.y = 0.9

color = Color()
color.r = 1.0
color.g = 0.0
color.b = 0.0
color.a = 1.0

canvas = black_canvas(100, 100)

print("all set up")

canvas = render_triangle(triangle, color, canvas)

print("triangle rendered")

export_image(canvas, "test")

print("writing file finished")