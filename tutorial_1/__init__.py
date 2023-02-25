def draw_circle(r):
    circle = ''
    for i in range(2 * r + 1):
        for j in range(2 * r + 1):
            if eq_circle(j, i, r):
                circle = circle + '* '
            else:
                circle = circle + '  '
        circle = circle + '\n'
    print(circle)


def eq_circle(x, y, r):
    return (pow(x, 2) +
     pow(y, 2) + pow(r, 2) -
      2 * r * (x + y)) <= 0


def donut(x, y, _r, r):
    return pow(x, 2) + pow(y, 2) + 
    pow(_r, 2) - 2 * _r * (x + y) <= 0 \
           and (pow(x, 2) + 
           pow(y, 2) + 2 * pow(_r, 2) - 2 * 
           _r * (x + y)) >= r * r


if __name__ == '__main__':
    draw_circle(15)
