def swap_halves(items):
    return items[len(items) // 2::] + items[:len(items) // 2]


def swap_at_index(items, k):
    return items[k + 1::] + items[:k + 1]


def rotate_k(items, k=1):
    li = list(items)
    for i in range(len(items)):
        li[(i + k) % len(items)] = items[i]
    return tuple(li)


def first_and_last_index(items, elem):
    return items.index(elem), len(items) - 1 - items[::-1].index(elem)


def reverse_first_and_last_halves(items):
    x = items[:len(items) // 2][::-1]
    y = items[len(items) // 2::][::-1]
    k = 0
    for j in range(len(x)):
        items[k] = x[j]
        k += 1
    for i in range(len(y)):
        items[k] = y[i]
        k += 1
    return items


print(reverse_first_and_last_halves([1, 2, 3, 4, 5, 6, 7, 8]))
