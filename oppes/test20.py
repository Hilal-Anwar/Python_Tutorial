def relation(file1, file2):
    """
    Determine the relationship between two files

    Arguments:
        file1, file2: strings, paths to two files
    Return:
        string: 'Equal', 'Subset' or 'No Relation'
    """
    f1 = open(file1, 'r')
    f2 = open(file2, 'r')
    x = f1.readlines()
    y = f2.readlines()
    count = 0
    for t in range(len(x)):
        if x[t] == y[t]:
            count += 1
    if len(x) == len(y) and count == len(x):
        return 'Equal'
    elif len(x) < len(y) and count > 1:
        return 'Subset'
    else:
        return 'No Relation'
