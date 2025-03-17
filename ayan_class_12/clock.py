import time
import math
from datetime import datetime


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return f"Point(x={self.x}, y={self.y})"


class Line:
    def __init__(self, point1, point2):
        self.point = point1
        self.slope = ((point2.y - point1.y)
                      / (point2.x - point1.x)) \
            if point2.x != point1.x else float('inf')

    def __str__(self):
        return (f"Line [{self.slope}x -"
                f" y {-self.slope * self.point.x + self.point.y}]")

    def contains(self, point):
        if ((self.slope == float('-inf') or self.slope == float('inf'))
                and abs(self.point.x - point.x) <= 0.01):
            return True
        return (point.y - self.point.y) == self.slope * (point.x - self.point.x) or \
            abs(point.y - self.point.y - self.slope * (point.x - self.point.x)) <= 0.01


def rotate(angle, center, point):
    angle = math.radians(angle)
    x, y = point.x, point.y
    X, Y = center.x, center.y
    arg = math.atan2(y - Y, x - X)
    d = arg - angle
    sqrt = math.sqrt((X - x) ** 2 + (Y - y) ** 2)
    return Point(center.x + (sqrt * math.cos(d)), center.y + (sqrt * math.sin(d)))


def main():
    R = 2
    c_r = 0.6
    r = 1.5
    local_time = datetime.now().strftime("%H:%M:%S")
    print(local_time)
    sec = Point(R, R - c_r)
    min = Point(R, R - c_r)
    hou = Point(R, R - c_r)
    sec = rotate(-datetime.now().second * 6, Point(R, R), Point(R, R - c_r))

    while True:
        local_time = datetime.now().strftime("%H:%M:%S")
        min = rotate(-int(local_time.split(':')[1]) * 6, Point(R, R), Point(R, R - c_r))
        hou = rotate(-int(local_time.split(':')[0]) * 30, Point(R, R), Point(R, R - c_r))
        s = []
        X_s, Y_s = sec.x, sec.y
        X_m, Y_m = min.x, min.y
        X_h, Y_h = hou.x, hou.y

        for y in range(int(2 * R * 100)):
            row = []
            for x in range(int(2 * R * 100)):
                I = ((y / 100) ** 2 + (x / 100) ** 2 +
                     2 * R ** 2 - 2 * R * ((x / 100) + (y / 100)) - r ** 2)
                K = ((y / 100) ** 2 + (x / 100) ** 2 + R ** 2 -
                     2 * R * ((x / 100) + (y / 100)))
                S = (y / 100) ** 2 + (x / 100) ** 2 - c_r ** 2 - 2 * (
                            (y / 100) * Y_s + (x / 100) * X_s) + X_s ** 2 + Y_s ** 2
                M = (y / 100) ** 2 + (x / 100) ** 2 - c_r ** 2 - 2 * (
                            (y / 100) * Y_m + (x / 100) * X_m) + X_m ** 2 + Y_m ** 2
                H = (y / 100) ** 2 + (x / 100) ** 2 - c_r ** 2 - 2 * (
                            (y / 100) * Y_h + (x / 100) * X_h) + X_h ** 2 + Y_h ** 2
                line_s = Line(Point(R, R), Point(X_s, Y_s))
                line_m = Line(Point(R, R), Point(X_m, Y_m))
                line_h = Line(Point(R, R), Point(X_h, Y_h))

                if ((K <= 0 <= I) or
                        (line_s.contains(Point(x / 100, y / 100)) and S < 0) or \
                        (line_m.contains(Point(x / 100, y / 100)) and M < 0) \
                        or (line_h.contains(Point(x / 100, y / 100)) and H < 0)):
                    row.append("██")
                else:
                    row.append("  ")
            s.append(''.join(row))

        print('\n'.join(s))
        sec = rotate(-6, Point(R, R), sec)
        print("\033[H", end="")
        #time.sleep(0.3)


if __name__ == "__main__":
    main()
