def draw_circle(r):
    for i in range(2 * r + 1):
        for j in range(2 * r + 1):
            if (eq_circle(j, i, r)):
                print(" * ", end='')
            else:
                print("   ", end='')
        print()


def eq_circle(x, y, r):
    return (pow(x, 2) + pow(y, 2) + pow(r, 2) - 2 * r * (x + y)) <= 0;

if __name__ == '__main__':
    R = 15;
    draw_circle(R)
