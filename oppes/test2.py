min = None


def find_min(items: list):
    mi = items[0]
    for item in items:
        if item < mi:
            mi = item
    return mi


def odd_increment_even_decrement_no_modify(items) -> list:
    return [x + 1 if x % 2 != 0 else x - 1 for x in items]


def odd_square_even_double_modify(items: list) -> list:
    for i in range(len(items)):
        if items[i] % 2 != 0:
            items[i] = items[i] ** 2
        else:
            items[i] = items[i] * 2
    return items


def more_than_two_unique_vowels(sentence):
    li = []
    l = sentence.split(',')
    for item in l:
        c = 0
        for char in item.lower():
            if char in 'aeiou':
                c += 1
        if c > 2:
            li.append(item)
    return set(li)


def sum_of_list_of_lists(lol):
    s = 0
    for item in lol:
        for char in item:
            s += char
    return s


def flatten(lol):
    return [char for item in lol for char in item]


def all_common(strings):
    li = ''
    for char in strings[0]:
        c = 0
        for s in strings:
            if char in s:
                c += 1
        if c == len(strings):
            li += char
    return li


def vocabulary(sentences):
    x = set()
    for word in sentences:
        for char in word.lower().split(' '):
            x.add(char)
    return sorted(x)

print(more_than_two_unique_vowels("functions,are,not,complicated"))