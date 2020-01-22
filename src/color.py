import math


class Color:
    def __init__(self):
        self.r: float = 0.0
        self.g: float = 0.0
        self.b: float = 0.0
        self.a: float = 0.0

    def to_pil(self):
        r: int = math.floor(self.r * 255.0)
        g: int = math.floor(self.g * 255.0)
        b: int = math.floor(self.b * 255.0)

        assert (0 <= r <= 255)
        assert (0 <= g <= 255)
        assert (0 <= b <= 255)

        return r, g, b


# combines colors; c1 on top of c2. Relies on c2.a == 1
def stack_colors(c1: Color, c2: Color) -> Color:
    assert (c2.a == 1)
    c3: Color = Color()
    c3.a = 1.0
    c3.r = c1.r * c1.a + c2.r * (1.0 - c1.a)
    c3.g = c1.g * c1.a + c2.g * (1.0 - c1.a)
    c3.b = c1.b * c1.a + c2.b * (1.0 - c1.a)
    return c3


def background() -> Color:
    result = Color()
    result.r = 0.0
    result.g = 0.0
    result.b = 0.0
    result.a = 1.0
    return result


def compare_color(c1: Color, c2: Color) -> float:
    assert c1.a == 1.0
    assert c2.a == 1.0
    delta_r: float = c1.r - c2.r
    delta_g: float = c1.g - c2.g
    delta_b: float = c1.b - c2.b

    return delta_r * delta_r + delta_g * delta_g + delta_b * delta_b


def from_pil(pil_color) -> Color:
    # (r, g, b) = ImageColor.getcolor(pil_color, "RGB")

    # this seems to work for the supplied images
    (r, g, b) = pil_color

    color = Color()
    color.r = r / 255.0
    color.g = g / 255.0
    color.b = b / 255.0
    color.a = 1.0

    return color
