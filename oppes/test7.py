def dict_from_string(string: str, key_type, value_type):
    '''
    Given a string where each line has a comma seperated key-value pair, create a dictionary out of it. Also convert the types of key and values to the given types.

    Arguments:
    string - str: string to be parsed
    key_type - class: the data type of the keys
    value_type - class: the data type of the values

    Return:
    D - dict: the output dictionary
    '''
    D = {}
    for line in string.split('\n'):
        D[key_type(line[:line.index(',')])] = value_type(line[line.index(',') + 1::])

    return D


dac = dict_from_string(string="""Apple,2
Banana,3
Orange,4
Grapes,3
Papaya,5""", key_type=str, value_type=int)

loop = map(lambda a, b: (a, b), dac.keys(),filter(lambda a: a % 2 == 0, dac.values()))
loop1 = filter(lambda a: a % 2 == 0, dac.values())
print(list(loop))
