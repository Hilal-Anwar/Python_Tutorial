def get_goals(filename, country):
    """
    Get the count of players and their cumulative goals for this country

    Arguments:
        filename: string
        country: string
    Return:
        result: tuple, (integer, integer)
    """
    x = (0, 0)
    file = open(filename, 'r')
    for line in file:
        line = line.replace('\n', '')
        words = line.split(',')
        if words[1] == country:
            x = (x[0] + 1, x[1] + int(words[2]))
    if x[0] == 0:
        return -1, -1
    else:
        return x
