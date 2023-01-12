def __heaps__permutation(arr, size):
    if size == 1:
        print(arr)
    else:
        for i in range(0, size):
            __heaps__permutation(arr, size - 1)
            swap__array(arr, size, i)


def swap__array(arr, size, i):
    if size % 2 != 0:
        tem = arr[0]
        arr[0] = arr[size - 1]
    else:
        tem = arr[i]
        arr[i] = arr[size - 1]
    arr[size - 1] = tem


if __name__ == '__main__':
    __heaps__permutation([2, 3, 5, 4], 4)
