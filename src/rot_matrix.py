import numpy as np


def rotmatrix(axis, angle):
    if not (0 < axis <= 3):
        raise IndexError("axis must be between 1 and 3")
    s, c = np.sin(angle), np.cos(angle)
    if axis == 1:
        matrix = [[1, 0, 0], [0, c, -s], [0, s, c]]
        return np.matrix(matrix)
    elif axis == 2:
        matrix = [[c, 0, -s], [0, 1, 0], [s, 0, c]]
        return np.matrix(matrix)
    else:
        matrix = [[c, -s, 0], [s, c, 0], [0, 0, 1]]
        return np.matrix(matrix)


def main():
    x = rotmatrix(2, 0.2)
    print(x)


if __name__ == "__main__":
    main()
