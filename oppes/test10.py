# mapping
def is_greater_than_5(numbers: list) -> list:
    '''Given a list of numbers, return a list of bools corresponding to whether the number is greater than 5'''
    return list(map(lambda x: x > 5, numbers))


# filtering
def filter_less_than_5(numbers: list) -> list:
    '''Given an list of numbers, return a list of numbers that are less than 5'''
    return list(filter(lambda x: x < 5, numbers))


# aggregation with filtering
def sum_of_two_digit_numbers(numbers: list):
    '''Given a list of numbers find the sum of all two_digit_numbers.
    '''
    return sum(list(filter(lambda x: x if 9 < x < 100 else 0, numbers)))


# aggregation with mapping
def is_all_has_a(words: list) -> bool:
    '''Given a list of words check if all words has the letter a(case insensitive) in it.
    '''
    return all(x.lower().count('a') >= 1 for x in words)


# enumerate
def print_with_numbering(items):
    '''
    Print a list in multiple lines with numbering.
    Eg. ["apple","orange","banana"]
    1. apple
    2. orange
    3. banana
    '''
    for item in items:
        print(str(items.index(item)+1)+'.', item)


# zip
def parallel_print(countries, capitals):
    '''
    Print the countries and capitals in multiple line seperated by a hyphen with space around it.
    '''
    for country, capital in zip(countries, capitals):
        print(country, '-', capital)


# key value list to dict
def make_dict(keys, values):
    '''Create a dict with keys and values'''
    d = {}
    for key, value in zip(keys, values):
        d[key] = value
    return d


# enumerate with filtering and map
def indices_of_big_words(words) -> list:
    '''Given a list of words, find the indices of the big words(length greater than 5).
    '''
    return [index for index, word in enumerate(words) if len(word) > 5]


# zip with mapping and aggregation
def decode_rle(chars: str, repeats: list) -> str:
    '''
    Create a string with i-th char from chars repeated i-th value of repeats number of times.

    Note rle refers to Run-length encoding
    '''
    return ''.join([(j * i) for i, j in zip(repeats, chars)])


print(is_all_has_a(['apple', 'orange', 'kiwi']))
