def index_of_first_occurance(row: list, elem):
    '''
    Given a list find the index of first occurance of 1 in it
    '''
    return row.index(elem)


def index_of_last_occurance(row: list, elem):
    '''
    Given a list find the index of last occurance of 1 in it.
    Hint: use index_of_first_one with reversal.
    '''
    return len(row) - 1 - row[::-1].index(elem)


def is_valid_coordinate(x: int, y: int, M):
    '''
    Checks if the x,y is a valid corrdinate(indices) in the matrix M(list of list). Assume coordinates are non-negative
    '''
    return 0 <= x < len(M) and 0 <= y < len(M[0])


def valid_adjacent_coordinates(x: int, y: int, M):
    '''
    Create a set of valid adjacent coordinates(indices) given x,y and a matrix M
    '''
    return {
        (x1, y1)
        for x1, y1 in [(x - 1, y), (x + 1, y), (x, y - 1), (x, y + 1)]  # all the possible adjacent coordinates
        if is_valid_coordinate(x1, y1, M)
    }


def next_coordinate_with_value(curr_coords, value, M, prev_coords=None):
    '''
    Find the coordinate(indices) of the next coordinate that has the `value` in it.
    For the starting coordinate the prev_coords would be None
    '''
    val_path = valid_adjacent_coordinates(curr_coords[0], curr_coords[1], M)
    if prev_coords is not None and val_path.__contains__(prev_coords):
        val_path.remove(prev_coords)
    for t in val_path:
        if M[t[0]][t[1]] == 1:
            return t


def get_path_coordinates(M):
    '''
    Given the matrix m, find the path formed by 1 from the last row to the first row.
    '''
    path = []
    x_start, x_end = len(M) - 1, 0
    y_start, y_end = index_of_last_occurance(M[-1], 1), index_of_first_occurance(M[0], 1)
    prev_coords = None
    cod = (x_start, y_start)
    path.append(cod)
    while cod != (x_end, y_end):
        t = cod
        cod = next_coordinate_with_value(cod, 1, M, prev_coords)
        path.append(cod)
        prev_coords = t
    return path


def print_path(M):
    path = get_path_coordinates(M)
    for cod in path:
        print(cod)


def alternate_path(M):
    path = get_path_coordinates(M)[1::2]
    for cod in path:
        M[cod[0]][cod[1]] = 2
    return M


def count_path(M):
    path = get_path_coordinates(M)
    count = 1
    for cod in path:
        M[cod[0]][cod[1]] = count
        count += 1
    return M


def mirror_horizontally(M):
    path = get_path_coordinates(M)
    for cod in path:
        M[cod[0]][len(M[0]) - 1 - cod[1]] = 1
    return M


def mirror_vertically(M):
    path = get_path_coordinates(M)
    for cod in path:
        M[len(M) - 1 - cod[0]][cod[1]] = 1
    return M


w = is_valid_coordinate(4, 1, [
    [0, 0, 1, 1],
    [0, 0, 0, 1],
    [1, 1, 1, 1],
    [1, 0, 0, 0],
    [1, 1, 0, 0]
])
print(w)
x = valid_adjacent_coordinates(4, 0, [
    [0, 0, 1, 1],
    [0, 0, 0, 1],
    [1, 1, 1, 1],
    [1, 0, 0, 0],
    [1, 1, 0, 0]
])
print(list(x))
print(next_coordinate_with_value((4, 0), 1, [
    [0, 0, 1, 1],
    [0, 0, 0, 1],
    [1, 1, 1, 1],
    [1, 0, 0, 0],
    [1, 1, 0, 0]
], (4, 1)))

print_path([
    [0, 0, 1, 1],
    [0, 0, 0, 1],
    [1, 1, 1, 1],
    [1, 0, 0, 0],
    [1, 1, 0, 0]
])
mirror_horizontally([
    [0, 1, 0, 0, 0],
    [0, 1, 1, 1, 0],
    [0, 0, 0, 1, 0],
    [0, 0, 0, 1, 1]
])
mirror_vertically([
    [0, 1, 0, 0, 0],
    [0, 1, 1, 1, 0],
    [0, 0, 0, 1, 0],
    [0, 0, 0, 1, 1]
])
