class Polynomial:
    def __init__(self, a: float, b: float):
        self._a = a
        self._b = b

    def at(self, x: float):
        return self._a * x + self._b
