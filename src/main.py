import random
import copy

from src.canvas import *
from src.genome import *

# set up reference
#input_file = "mona_lisa_small.png"
input_file = "test.png"
reference = import_image(input_file)

export_image(reference, "reference")

width: int = reference.width
height: int = reference.height

# set up genome
genome = Genome()

num_triangles: int = 5
for n in range(num_triangles):
    triangle = Triangle()
    triangle.v1.x = random.random()
    triangle.v1.y = random.random()
    triangle.v2.x = random.random()
    triangle.v2.y = random.random()
    triangle.v3.x = random.random()
    triangle.v3.y = random.random()

    color = Color()
    color.r = random.random()
    color.g = random.random()
    color.b = random.random()
    color.a = random.random()

    genome.triangles.append(triangle)
    genome.colors.append(color)

canvas = genome.render(width, height)
export_image(canvas, "generation_0")

previous_error: float = compare_canvas(reference, canvas)

# start optimizing
num_iterations: int = 10000000

prev_written: int = 0
for n in range(num_iterations):
    print(n)

    genome2 = copy.deepcopy(genome)
    genome2.mutate()
    canvas = genome2.render(width,height)
    current_error: float = compare_canvas(reference, canvas)

    if current_error <= previous_error:
        genome = genome2
        previous_error = current_error
        if n - prev_written > 10:
            export_image(canvas, "generation_{}".format(n+1))
            prev_written = n

