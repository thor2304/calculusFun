from Regression import Linear_Regression
from Regression.Coordinate import Coordinate
from Regression.Polynomial import Polynomial


def main():
    test_func = Polynomial(4, 30)

    coordinates = [
        Coordinate(1, test_func.at(1) + 0.05),
        Coordinate(2, test_func.at(2)),
        Coordinate(3, test_func.at(3)),
    ]

    result = Linear_Regression.perform_regression(coordinates)

    print(coordinates)
    print(result)


if __name__ == '__main__':
    main()
