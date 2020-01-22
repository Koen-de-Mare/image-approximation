import math

class Color:
    def __init__(self):
        self.r: float = 0.0
        self.g: float = 0.0
        self.b: float = 0.0
        self.a: float = 0.0

    #def to_pil(self) -> tuple[int, int, int]:
    def to_pil(self):
        r: int = math.floor(self.r * 255.0)
        g: int = math.floor(self.g * 255.0)
        b: int = math.floor(self.b * 255.0)

        assert (0 <= r <= 255)
        assert (0 <= g <= 255)
        assert (0 <= b <= 255)

        return (r,g,b)


# combines colors; c1 on top of c2. Relies on c2.a == 1
def stack_colors(c1: Color, c2: Color) -> Color:
    assert(c2.a == 1)
    c3: Color = Color()
    c3.a: float = 1.0
    c3.r: float = c1.r * c1.a + c2.r * (1.0 - c1.a)
    c3.g: float = c1.g * c1.a + c2.g * (1.0 - c1.a)
    c3.b: float = c1.b * c1.a + c2.b * (1.0 - c1.a)
    return c3

def black() -> Color:
    result = Color()
    result.r: float = 0.5
    result.g: float = 0.5
    result.b: float = 0.5
    result.a: float = 1.0
    return result

def from_pil(pil_color) -> Color:
    (r, g, b) = pil_color.getrgb()

    color = Color()
    color.r = r / 255.0
    color.g = g / 255.0
    color.b = b / 255.0
    color.a = 1.0

    return color

