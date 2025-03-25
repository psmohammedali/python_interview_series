def quick_sort(my_list, si, ei):
    if si >= ei:
        return

        # at this point, the list has more than 2 elements
    pivot = my_list[si]
    ri = si + 1
    count = 0
    while ri <= ei:
        if my_list[ri] < pivot:
            count += 1
        ri += 1

    # making it reach the pivot element to its correct position
    my_list[si], my_list[si + count] = my_list[si + count], my_list[si]
    pivot_index = si + count
    # now making all elements left to the pivot smaller to it and vice versa
    left = si
    right = ei
    while left < pivot_index < right:
        if my_list[left] < my_list[pivot_index]:
            left += 1
        elif my_list[right] >= my_list[pivot_index]:
            right = right - 1
        else:
            # at this point, swapping can be done
            my_list[left], my_list[right] = my_list[right], my_list[left]

    quick_sort(my_list, si, pivot_index - 1)
    quick_sort(my_list, pivot_index + 1, ei)


my_list = [3, 2, 8, 47, 1, 9, 6, 4,9]
quick_sort(my_list, 0, len(my_list) - 1)
print(my_list)
