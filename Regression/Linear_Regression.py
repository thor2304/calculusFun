from Regression.Coordinate import Coordinate


def perform_regression(inputs: list[Coordinate]):
    n = len(inputs)

    sum_x = _sum(inputs, "x")
    sum_y = _sum(inputs, "y")
    sum_x_y_multiplied = _multiplied_sum(inputs, "x", "y")
    sum_x_squared = _multiplied_sum(inputs, "x", "x")

    m_numerator = (sum_y * sum_x) - (n * sum_x_y_multiplied)
    m_denom = (sum_x * sum_x) - (n * sum_x_squared)

    m = m_numerator / m_denom

    b = (sum_y - m * sum_x) / n

    return m, b


def _sum(inputs: list[Coordinate], x_or_y: str):
    out = 0
    for coordinate in inputs:
        out += coordinate.get(x_or_y)

    return out


def _multiplied_sum(inputs: list[Coordinate], x_or_y1: str, x_or_y2: str):
    out = 0
    for coordinate in inputs:
        out += coordinate.get(x_or_y1) * coordinate.get(x_or_y2)

    return out
