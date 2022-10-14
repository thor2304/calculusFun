from __future__ import annotations
from typing import Union


class Fraction:
    def __init__(self, top: int, bottom: int):
        self._top = top
        self._bottom = bottom

    def as_float(self) -> float:
        return self._top / self._bottom

    def get_top(self):
        return self._top

    def get_bottom(self):
        return self._bottom

    def flip_sign(self) -> Fraction:
        return Fraction(-self._top, - self._bottom)

    def add_fraction(self, other: Fraction) -> Fraction:
        return Fraction(self._top + other.get_top(), self._bottom + other.get_bottom())

    def subtract_fraction(self, other: Fraction) -> Fraction:
        return self.add_fraction(other.flip_sign())

    def add_int(self, number: int) -> Fraction:
        return self.add_fraction(Fraction(number, 1))

    def subtract_int(self, number: int) -> Fraction:
        return self.add_fraction(Fraction(-number, 1))

    def multiply(self, other: Union[int, Fraction]) -> Fraction:
        if other is Fraction:
            return Fraction(self._top * other._top, self._bottom * other._bottom)
        else:
            return Fraction(self._top * other, self._bottom)

    def divide(self, other: Union[int, Fraction]) -> Fraction:
        if other is Fraction:
            new_frac = Fraction(other._bottom, other._top)
        else:
            new_frac = Fraction(1, other)

        return self.multiply(new_frac)

    def __mul__(self, other: Union[int, Fraction]) -> Fraction:
        return self.multiply(other)

    def __truediv__(self, other: Union[int, Fraction]) -> Fraction:
        return self.divide(other)
    
    def __add__(self, other: Union[int, Fraction]) -> Fraction:
        if other is Fraction:
            return self.add_fraction(other)
        else:
            return self.add_int(other)

    def __sub__(self, other: Union[int, Fraction]) -> Fraction:
        if other is Fraction:
            return self.subtract_fraction(other)
        else:
            return self.subtract_int(other)


if __name__ == '__main__':
    frac = Fraction(1, 2)
