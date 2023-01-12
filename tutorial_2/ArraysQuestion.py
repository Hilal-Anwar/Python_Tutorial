def is_all_elements_equal(arr1, arr2):
    if len(arr1) != len(arr2):
        return False
    else:
        return arr1.sort().__eq__(arr2.sort())


if __name__ == '__main__':
    print(is_all_elements_equal([5, 3, 7], [7, 3, 5]))
