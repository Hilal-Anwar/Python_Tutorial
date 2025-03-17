def sum_of_squares(numbers):
    return sum(x * x for x in numbers)


def total_cost(cart):
    return sum(a[0] * a[1] for a in cart)


def abbreviation(sentence):
    ab = ''.join([x[0].capitalize() + '.' for x in sentence.split(' ')])
    return ab


def palindromes(words):
    return [word for word in words if word[::-1] == word]


def all_chars_from_big_words(sentence):
    x = {y for word in sentence.lower().split(' ') if len(word) > 5 for y in word}
    return set(sorted(x))


def flatten(lol):
    li = [j for i in lol for j in i]
    return li


def unflatten(items, n_rows):
    lii = [[items[j] for j in range(i, i + len(items) // n_rows)] for i in range(0, len(items), len(items) // n_rows)]
    return lii


def make_identity_matrix(m):
    li = [[1 if j == i else 0 for j in range(m)] for i in range(m)]
    return li


def make_lower_triangular_matrix(m):
    li = [[j + 1
           if j <= i
           else 0
           for j in range(m)]
          for i in range(m)]
    return li
