class Color:
    def __init__(self):
        self.r: float = 0.0
        self.g: float = 0.0
        self.b: float = 0.0
        self.a: float = 0.0

# combines colors; c1 on top of c2. Relies on c2.a == 1
def stack_colors(c1: Color, c2: Color) -> Color:
    assert(c2.a == 1)
    c3 = Color
    c3.a = 1.0
    c3.r = c1.r * c1.a + c2.r * (1.0 - c1.a)
    c3.g = c1.g * c1.a + c2.g * (1.0 - c1.a)
    c3.b = c1.b * c1.a + c2.b * (1.0 - c1.a)
    return c3

def black():
    result = Color()
    result.r = 0.0
    result.g = 0.0
    result.b = 0.0
    result.a = 0.0