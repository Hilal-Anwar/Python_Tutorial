def get_scores(filename, index):
    f = open(filename, 'r')
    # Ignore the header
    f.readline()
    # we are now at the beginning of the second line of the file

    scores = []
    line = f.readline()
    while line != '':
        L = line.strip().split(',')
        scores.append(int(L[index]))
        line = f.readline()

    f.close()
    return scores
def do_something(L):
    L.sort()
    mid = len(L) // 2
    if len(L) % 2 == 0:
        return (L[mid] + L[mid - 1]) // 2
    else:
        return L[mid]
print(do_something(get_scores('scores.csv', 4)))