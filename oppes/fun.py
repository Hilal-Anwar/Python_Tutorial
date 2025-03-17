def walk_matrix(M, shape):
    """
    Walk along the matrix M according to the specified shape and return the path.

    Args:
        M (list of lists): The square matrix.
        shape (str): Path shape, one of "L", "O", or "Z".

    Returns:
        list: Path along the matrix according to the shape.
    """
    ...
    if shape == 'L':
        return get_col(M, 0)[0: len(M) - 1] + get_row(M, len(M) - 1)
    elif shape == 'O':
        return get_row(M, 0) + get_col(M, len(M) - 1)[1:] + (get_row(M, len(M) - 1)[::-1])[1:] + (get_col(M, 0)[::-1][1:len(M)-1])
    elif shape == 'Z':
        return get_row(M, 0)[0: len(M) - 1] + get_right_diagonal(M) + get_row(M, len(M) - 1)[1: len(M)]


def get_row(M, i):
    return M[i]


def get_col(M, j):
    col = []
    for i in range(len(M)):
        col.append(M[i][j])
    return col


def get_right_diagonal(M):
    right_diagonal = []
    j = len(M[0]) - 1
    i = 0
    while j >= 0:
        right_diagonal.append(M[i][j])
        j -= 1
        i += 1
    return right_diagonal


Mat = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
print(walk_matrix(Mat, 'Z'))
