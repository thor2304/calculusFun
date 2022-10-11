from __future__ import annotations


class Matrix:
    def __init__(self, elements: list[list[float]]):
        self._storage = elements
        #     ensure that the arrays are square
        #     if not square pad with zeros and print the diff
        self._num_rows = len(self._storage)
        self._num_cols = len(self._storage[0])

    def matrix_multiply(self, matrix_b: Matrix) -> Matrix:
        # Check that matrix size matches
        # Multiply with rules from Calculus classes
        pass

    def matrix_add(self, matrix_b: Matrix) -> Matrix:
        # Check that matrix size matches
        # Multiply with rules from Calculus classes
        pass

    def det(self) -> float:
        #     Ensure matrix size allows det calculation
        #     use rules from calculus classes
        #     Transform matrix to simpler forms until 2x2 then compute
        pass

    def get_inverse(self) -> Matrix:
        # Use rules from Calculus classes
        pass

    def get_transposed(self) -> Matrix:
        # Use rules from calculus class
        pass

    def num_rows(self) -> int:
        return self._num_rows

    def num_cols(self) -> int:
        return self._num_cols
