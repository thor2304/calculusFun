from __future__ import annotations

import time
from typing import Union


class Matrix:
    def __init__(self, elements: list[list[float]]):
        self._storage = elements
        #     ensure that the arrays are square
        #     if not square pad with zeros and print the diff
        self._num_rows = len(self._storage)
        self._num_cols = len(self._storage[0])
        self._ensure_square()

    def _ensure_square(self):
        num_cols_max = 0
        for i in self._storage:
            if len(i) > num_cols_max:
                num_cols_max = len(i)

        if num_cols_max is self._num_cols:
            return

        for i in range(self._num_rows):
            for j in range(0, num_cols_max - len(self._storage[i])):
                self._storage[i].append(0)

        self._num_cols = num_cols_max

    def __repr__(self):
        # Complete repr by actually ordering the numbers such that columns look correct
        number_rep = ""
        for i in self._storage:
            for j in i:
                number_rep += f" {j} "
            number_rep += "\n"
        return f"Matrix with size: {self.size()} With numbers: \n{number_rep}"

    def get_number(self, col: int, row: int, math_numbering: bool = True) -> float:
        correcting_number = 1 if math_numbering else 0
        return self._storage[row - correcting_number][col - correcting_number]

    def set_number(self, col: int, row: int, value: float, math_numbering: bool = True):
        correcting_number = 1 if math_numbering else 0
        self._storage[row - correcting_number][col - correcting_number] = value

    def __add__(self, matrix_b: Matrix) -> Matrix:
        # Check that matrix size matches
        if str(self.size()) != str(matrix_b.size()):
            raise Exception(f"Matrix sizes {self.size()} and {matrix_b.size()} does not match")

        # Create matrix to put results into
        out_matrix = Matrix([x for x in self._storage])

        for i in range(0, self.num_rows()):
            for j in range(0, self.num_cols()):
                result = self.get_number(j, i, False) + matrix_b.get_number(j, i, False)
                out_matrix.set_number(j, i, result, False)

        return out_matrix

    def __mul__(self, other: Union[float, int, Matrix]) -> Matrix:
        # Check that matrix size matches
        # Multiply with rules from Calculus classes

        new_matrix = Matrix([x for x in self._storage])

        if type(other) is Matrix:
            raise ValueError("Not yet implemented for matrice")
        elif not (type(other) == int or type(other) == float):
            raise ValueError("Must be float or int or matrix")
        else:
            for j in range(0, self.num_cols()):
                for i in range(0, self.num_rows()):
                    new_num = self.get_number(j, i, False) * other
                    new_matrix.set_number(j, i, new_num, False)

        return new_matrix

    def __sub__(self, other: Union[float, Matrix]) -> Matrix:
        if other is Matrix:
            return self + (other * -1)

    def det(self) -> float:
        #     Ensure matrix size allows det calculation
        #     use rules from calculus classes
        #     Transform matrix to simpler forms until 2x2 then compute
        pass

    def get_upper_triangular_form(self) -> Matrix:
        # Brute force recipe on slides from lecture 5
        pass

    def get_inverse(self) -> Matrix:
        # Use rules from Calculus classes
        # Gauss-jordan can be used
        pass

    def get_transposed(self) -> Matrix:
        # Use rules from calculus class
        pass

    def num_rows(self) -> int:
        """Correctly returns the number of rows in the matrix"""
        return self._num_rows

    def num_cols(self) -> int:
        """Correctly returns the number of columns in the matrix"""
        return self._num_cols

    def size(self) -> tuple[int, int]:
        return self._num_cols, self._num_rows


if __name__ == '__main__':
    matrix = Matrix(
        [
            [1, 2, 3],
            [3, 2, 1],
            [4, 5, 6, 9, 8, 1]
        ]
    )

    matrixB = Matrix(
        [
            [1, 2, 3, 4],
            [3, 2, 1, 4],
            [4, 5, 6, 4],
        ]
    )

    # print(matrix.size() == matrixB.size())
    # print(matrixB.num_cols())
    # print(matrixB.num_rows())
    print(matrixB)

    print(matrix)
    print(matrix.get_number(1, 2))
    matrix.set_number(1, 2, 7)
    print(matrix.get_number(1, 2))

    matrixB = Matrix(
        [
            [1, 2],
            [3, 4],
            [4, 5],
        ]
    )

    matrix = Matrix(
        [
            [10, 20],
            [30, 40],
            [60, 50],
        ]
    )

    print(matrixB)
    print(matrix)

    print(matrix * 2)
    print(matrix * matrixB)
