from PIL import Image

#from src import color
from src.vector import Vector,dot
from src.triangle import Triangle

print("Hello world")


# PIL

image_path: str = "input images/mona_lisa_small.png"
im = Image.open(image_path)
print(im.format, im.size, im.mode)


# Vector

v1 = Vector(1.0, 2.0)
v2 = Vector(3.0, 4.0)

print(v1.show())
print(v2.show())

print("dot product: {}".format(dot(v1,v2)))

v3 = v1.add(v2)
print(v3.show())


# Triangle

t1 = Triangle()
print(t1.show())

t1.v1.x = 10.0
t1.v1.y = 10.0
t1.v2.x = 20.0
t1.v2.y = 10.0
t1.v3.x = 10.0
t1.v3.y = 20.0

v = Vector()
v.x = 14.0
v.y = 14.0
print("contains {}".format(t1.contains(v)))
