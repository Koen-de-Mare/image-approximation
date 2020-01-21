class Vector:
    def __init__(self, x=0.0, y=0.0):
        self.x: float = x
        self.y: float = y

    def show(self) -> str:
        return "x: {}, y: {}".format(self.x, self.y)

    def add(self, rhs: 'Vector') -> 'Vector':
        result = Vector()
        result.x = self.x + rhs.x
        result.y = self.y + rhs.y
        return result

    def sub(self, rhs: 'Vector') -> 'Vector':
        result = Vector()
        result.x = self.x - rhs.x
        result.y = self.y - rhs.y
        return result

    def neg(self) -> 'Vector':
        result = Vector()
        result.x = -self.x
        result.y = -self.y
        return result

    def mul(self, a: float) -> 'Vector':
        result = Vector()
        result.x = self.x * a
        result.y = self.y * a
        return result

def dot(v1: Vector, v2: Vector) -> float:
    return v1.x * v2.x + v1.y * v2.y

# from two vectors (provided being linearly independent), makes a conjugate (relatively contravariant) pair
#def make_conjugate(v1: Vector, v2: Vector) -> tuple[Vector, Vector]:
def make_conjugate(v1: Vector, v2: Vector):
    v1_rot = Vector()
    v1_rot.y = v1.x
    v1_rot.x = -v1.y

    v2_rot = Vector()
    v2_rot.y = v2.x
    v2_rot.x = -v2.y

    # observe that the indices 1 and 2 are mixed, since dot(v1, v1_rot) = 0, so v1_rot proportional to v2_conj
    v1_conj = v2_rot.mul(1.0 / dot(v1, v2_rot))
    v2_conj = v1_rot.mul(1.0 / dot(v2, v1_rot))

    return (v1_conj, v2_conj)
