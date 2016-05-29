from collections import namedtuple

N = 2
A = [
    [1, 0, 2],
    [0, 1, 3]
]


def equation(xs, a_eq):
    sumA = 0
    for i in range(N):
        sumA += a_eq[i] * xs[i]
    sumA += a_eq[-1]
    return sumA


def get_sings(res):
    result = []
    for r in res:
        result.append('+' if r > 0 else '-')
    return result


Point = namedtuple('Point', ['x', 'y'])
Point.val = lambda p: (p.x, p.y)

class Square():

    def __init__(self, p0, p1, p2, p3):
        self.r_up = p0
        self.l_up = p1
        self.r_down = p2
        self.l_down = p3
        self.square = (self.r_up, self.l_up, self.r_down, self.l_down)

    def break_square(self):
        center, center_up, center_left, center_right, center_down = self.get_center()
        r_up = Square(self.r_up, center_up, center_right, center)
        l_up = Square(center_up, self.l_up, center, center_left)
        r_down = Square(center_right, center, self.r_down, center_down)
        l_down = Square(center, center_left, center_down, self.l_down)
        for square in [r_up, l_up, r_down, l_down]:
            yield square

    def get_center(self):
        x = (self.l_up.x + self.r_up.x) / 2
        y = (self.l_down.y + self.l_up.y) / 2

        center = Point(x, y)
        center_up = Point(center.x, self.r_up.y)
        center_left = Point(self.l_up.x, center.y)
        center_right = Point(self.r_up.x, center.y)
        center_down = Point(center.x, self.r_down.y)

        return center, center_up, center_left, center_right, center_down

    def __iter__(self):
        for p in self.square:
            yield p

    def __str__(self):
        return "{}, {}, {}, {}".format(*map(tuple, self.square))


def process_square(square, previous_signs=None):
    current_signs = []
    for a_eq in A:
        res = []
        for point in square:
            res.append(equation(point.val(), a_eq))
        signs = get_sings(res)
        current_signs.append(signs)
    if current_signs == previous_signs:
        return None
    for sub_square in square.break_square():
        res = process_square(sub_square, current_signs)
        if res is None:
            print(sub_square, "without solution!")
            continue
        else:
            print("solution found!", sub_square)
            raise ValueError("Solution found!")


def main():
    s = Square(Point(100, 100), Point(-100, 100), Point(100, -100), Point(-100, -100))
    # s = Square(Point(-100, -100), Point(0, -100), Point(0, 0), Point(-100, 0))
    process_square(s)

if __name__ == '__main__':
    main()
