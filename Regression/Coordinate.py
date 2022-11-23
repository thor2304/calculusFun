from __future__ import annotations

from typing import Union


class Coordinate:
    def __init__(self, x: float, y: float):
        self._x = x
        self._y = y

    def get_x(self):
        return self._x

    def get_y(self):
        return self._y

    def get(self, x_or_y: str):
        if x_or_y == "x":
            return self.get_x()
        elif x_or_y == "y":
            return self.get_y()
        else:
            raise ValueError(f"{x_or_y} is not either x or y")

    def __repr__(self):
        return f"({self._x}, {self._y})"
