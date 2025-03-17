def list_mutating_operations(items: list, item1, item2):
    # sort the `items` inplace
    ...
    print("sorted:", sorted(items))

    # add item1 to the `items` at the end
    items.append(item1)
    print("append:", items)
    # add item2 at index 3
    items.insert(3, item2)
    print("insert:", items)

    # extend `items` with the first three elements in `items`
    items=items + items[:3]
    print("extend:", items)

    # pop the fifth element and store it in variable `popped_item`
    popped_item = items.pop(5)
    print("pop:",items)

    # remove first occurance of `item2` from the list
    items.remove(item2)
    print("remove:",items)

    # make the element at index 4 None
    ...
    print("modify_index:",items)

    # make the even indices None
    ...
    print("modify_slice:",items)

    # delete the third last element
    ...
    print("delete_index:",items)

    # delete the even indices
    ...
    print("delete_slice:",items)

    return items, popped_item

def list_non_mutating_operations(items:list, item1, item2):

    # print the sorted version of items
    print("sorted:",...)

    # print a lsit with item1 appended to the `items` at the end
    print("append:",...)

    # print a list with item2 added to items at index 3
    print("insert:",...)

    # print a list with the first three elements in `items` added to the end of the `items` again
    print("extend:", ...)

    #  print a list with the fifth element from `items` removed
    print("pop:",...)

    # print a list with first occurance of `item2` removed from `items`

    print("remove:",...) # hint: you may want to use index

    # print a list with the fourth element of `items` changed to None
    print("modify_index:",...)

    # print a list with the even indices changed to None

    print("modify_slice:",...)

    # print a list with the even indices removed
    print("delete_slice:",...)

    return items

def do_set_operation(set1, set2, set3, item1, item2):
    # add item1 to set1
    ...
    print(sorted(set1))
    # remove item2 from set1. What if item2 is not in set1?
    ...
    print(sorted(set1))

    # add elements from set2 to set1
    ...
    print(sorted(set1))

    # remove all elements from set1 that are in set3
    ...
    print(sorted(set1))

    # print the common elements in both set2 and set3 as a sorted list.
    print(...)

    # print all unique elements present in set1, set2 an set3 as a sorted list
    print(...)

    # print all unique elements that are in set2 but not in set3 as a sorted list
    print(...)

    # print all the non common elements from both set2 and set3
    print(...)

    return set1,sorted(set1),sorted(set2),sorted(set3)
