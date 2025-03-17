def do_something(filename):
    f = open(filename, 'r')
    maxword = f.readline().strip()
    count = 1
    # we are now at the beginning of the second line
    for line in f:
        word = line.strip()
        if len(word) > len(maxword):
            maxword = word
            count = 1
        elif len(word) == len(maxword):
            count += 1

    f.close()
    return count


print(do_something(' words.txt'))