import numpy as np


class point:
    def __init__(self, position):
        if len(position) != 3:
            raise IndexError("length must be 3")
        self.position = np.matrix(position).transpose()
        self.ipos = self.position

    @property
    def visual(self):
        return self.position[2, 0] >= 0

    def matrix_apply(self, matrix):
        self.position = matrix*self.position

    def reset(self):
        self.position = self.ipos

    def project(self, focal_len):
        z = self.position[2, 0]
        self.pos2d = self.position[:2, 0]
        self.pos2d = self.pos2d*focal_len/z


def main():
    x = point([1, 2, 3])
    print(x.position)
    print(x.visual)
    x.project(10)
    print(x.pos2d)


if __name__ == "__main__":
    main()
