from collections import namedtuple
import math

N = 2
E = 0.000001
A = [
    [1, 0, 2],
    [0, 1, 3]
]


def equation(xs, a_eq):
    sumA = 0
    for i in range(N):
        sumA += a_eq[i] * xs[i]
    sumA -= a_eq[-1]
    return sumA


def get_binary_sings(res):
    return tuple(1 if r > 0 else 0 for r in res)


Point = namedtuple('Point', ['x', 'y'])
Point.val = lambda p: (p.x, p.y)
Point.round = lambda p: [round(i) for i in p.val()]

class Square():

    def __init__(self, p0, p1, p2, p3):
        self.r_up = p0
        self.l_up = p1
        self.r_down = p2
        self.l_down = p3
        self.square = (self.r_up, self.l_up, self.r_down, self.l_down)

    def break_square(self):
        center, center_up, center_left, center_right, center_down = self.get_center_cross()
        r_up = Square(self.r_up, center_up, center_right, center)
        l_up = Square(center_up, self.l_up, center, center_left)
        r_down = Square(center_right, center, self.r_down, center_down)
        l_down = Square(center, center_left, center_down, self.l_down)
        for square in [r_up, l_up, r_down, l_down]:
            yield square

    def get_center_cross(self):

        center = self.get_center()
        center_up = Point(center.x, self.r_up.y)
        center_left = Point(self.l_up.x, center.y)
        center_right = Point(self.r_up.x, center.y)
        center_down = Point(center.x, self.r_down.y)

        return center, center_up, center_left, center_right, center_down

    def get_center(self):
        x = (self.l_up.x + self.r_up.x) / 2
        y = (self.l_down.y + self.l_up.y) / 2
        return Point(x, y)

    def __iter__(self):
        for p in self.square:
            yield p

    def __str__(self):
        return "{}, {}, {}, {}".format(*map(tuple, self.square))

def norm(ar):
    s = 0
    for elem in ar:
        s += elem**2
    return math.sqrt(s)

def stop_condition(square):
    res = []
    for a_eq in A:
        res.append(equation(square.get_center().val(), a_eq))
    return norm(res) < E


SIGNS_TO_STATUS_MAP = {
    (1, 1): False,
    (0, 1): False,
    (1, 0): False,
    (0, 0): False
}

def process_square(square):
    signs_map = {**SIGNS_TO_STATUS_MAP}
    for point in square:
        res = []
        for a_eq in A:
            res.append(equation(point.val(), a_eq))
        signs = get_binary_sings(res)
        if signs in signs_map:
            signs_map[signs] = True

    if stop_condition(square):
        return (True, square)

    if all(signs_map.values()):
        for sub_square in square.break_square():
            success, square = process_square(sub_square)
            if success:
                print("Solution found!", square.get_center().round())
    return (False, None)


def main():
    s = Square(Point(100, 100), Point(-100, 100), Point(100, -100), Point(-100, -100))
    # s = Square(Point(-100, -100), Point(0, -100), Point(0, 0), Point(-100, 0))
    process_square(s)

if __name__ == '__main__':
    main()
