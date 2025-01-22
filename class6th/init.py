def binary_pascal(size):
    s = ""
    for i in range(size + 1):
        s = s + (" " * (size - i))
        f = 1
        s = s + str(f) + " "
        for j in range(1, i + 1):
            f *= (i - j + 1) / j
            s = s + (str(int(f % 2)) + " ")
        s = s + '\n'
    return s
print(binary_pascal(600))
