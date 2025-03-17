def num_to_words(mat):
    """
    Convert matrix to file

    Argument:
        mat: list of lists
    Return:
        None
    """
    num = {1: 'one', 2: 'two', 3: 'three', 4: 'four', 5: 'five', 6: 'six', 7: 'seven', 8: 'eight', 9: 'nine'}
    file = open('words.csv', 'w')
    for r in range(len(mat)):
        s = ''
        for c in range(len(mat[0])):
            if c != len(mat[r]) - 1:
                s += num[mat[r][c]] + ','
            else:
                s += num[mat[r][c]]
        if r != len(mat) - 1:
            file.write(s + '\n')
        else:
            file.write(s)
    file.close()
    return file


print(num_to_words([[1, 2, 3], [4, 5, 6], [7, 8, 9]]))
