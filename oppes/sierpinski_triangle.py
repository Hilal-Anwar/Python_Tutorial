def sierpinski_triangle(size):
    start = size
    end = size
    s = []
    val = []
    t = 0
    for i in range(size + 1):
        c = 0
        k = 0
        val = pascal(val)
        line = []
        for j in range(end + 1):
            if j >= start:
                if c == 0:
                    num = val[k]
                    line.append(get_color(t) +
                                str("█") +
                                "\033[0m"
                                if num == 1 else " ")
                    c = 1
                    k += 1
                else:
                    line.append(" ")
                    c = 0
            else:
                line.append(" ")
        if (i + 1) % 4 == 0:
            t = 0 if t == 7 else t + 1
        start -= 1
        end += 1
        s.append("".join(line))
    return "\n".join(s)


def pascal(a):
    tem = [1] * (len(a) + 1)
    for i in range(1, len(a)):
        tem[i] = (a[i - 1] + a[i]) % 2
    return tem


def get_color(i):
    color = ["\033[0;31m", "\033[0;32m", "\033[0;33m", "\033[0;34m",
             "\033[0;35m", "\033[0;36m", "\033[0;97m", "\033[0;96m"]
    return color[i]


if __name__ == "__main__":
    print(sierpinski_triangle(500))
