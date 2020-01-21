from src import vector
from vector import Vector

class Triangle:
    def __init__(self):
        self.v1: Vector = vector.Vector()
        self.v2: Vector = vector.Vector()
        self.v3: Vector = vector.Vector()

    def show(self) -> str:
        return "v1: {}, v2: {}, v3: {}".format(self.v1.show(), self.v2.show(), self.v3.show())

    def contains(self, v: Vector) -> bool:
        v2_prime: Vector = self.v2.sub(self.v1)
        v3_prime: Vector = self.v3.sub(self.v1)
        v_prime:  Vector = v.sub(self.v1)

        # find c2, c3 such that v_prime = c2 * v2_prime + c3 * v3_prime
        (v2_prime_conj, v3_prime_conj) = vector.make_conjugate(v2_prime, v3_prime)
        c2 = vector.dot(v_prime, v2_prime_conj)
        c3 = vector.dot(v_prime, v3_prime_conj)

        return c2 > 0.0 and c3 > 0.0 and c2 + c3 < 1.0

