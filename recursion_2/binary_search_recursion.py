def binary_search(my_list, search_ele, start, end):
    if start > end:
        return -1

    mid = (start + end) // 2
    if my_list[mid] == search_ele:
        return mid

    # basically the ele may find in the left side of the mid
    if my_list[mid] > search_ele:
        my_small_output = binary_search(my_list, search_ele, start, mid - 1)
        return my_small_output

    else:
        my_small_output = binary_search(my_list, search_ele, mid + 1, end)
        return my_small_output


my_list = [1,5,7,9,11,13,58]
print(binary_search(my_list, 9, 0, len(my_list) - 1))
