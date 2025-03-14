def merge_2_list(left_sorted_list,right_sorted_list):
    left_index = 0
    right_index = 0
    limit = min(len(left_sorted_list), len(right_sorted_list))
    new_list = []

    # print(left_sorted_list, right_sorted_list)
    while left_index < len(left_sorted_list) and right_index < len(right_sorted_list):
        if left_sorted_list[left_index] < right_sorted_list[right_index]:
            new_list.append(left_sorted_list[left_index])
            left_index += 1
        else:
            new_list.append(right_sorted_list[right_index])
            right_index += 1

    while left_index < len(left_sorted_list):
        new_list.append(left_sorted_list[left_index])
        left_index += 1

    while right_index < len(right_sorted_list):
        new_list.append(right_sorted_list[right_index])
        right_index += 1

    return new_list



def merge_sorting(my_list):
    if len(my_list) == 0 or len(my_list) == 1:
        return my_list

    mid = len(my_list) // 2
    left_list = my_list[:mid]
    right_list = my_list[mid:]
    # print(left_list, right_list)
    left_sorted_list = merge_sorting(left_list)
    right_sorted_list = merge_sorting(right_list)

    left_index = 0
    right_index = 0
    limit = min(len(left_sorted_list), len(right_sorted_list))
    new_list = []

    # print(left_sorted_list, right_sorted_list)
    while left_index < limit and right_index < limit:
        if left_sorted_list[left_index] < right_sorted_list[right_index]:
            new_list.append(left_sorted_list[left_index])
            left_index += 1
        else:
            new_list.append(right_sorted_list[right_index])
            right_index += 1

    print(left_sorted_list,right_sorted_list)
    while left_index < len(left_sorted_list):
        new_list.append(left_sorted_list[left_index])
        left_index += 1

    while right_index < len(right_sorted_list):
        new_list.append(right_sorted_list[right_index])
        right_index += 1

    return new_list


# my_list = [1, 4, 2, 1, 5, 5, 58, 8, 3, 4, 2, 0, 1, 2, 34]
my_list = merge_2_list([1, 1, 2, 4, 5, 5, 58], [0, 1, 2, 2, 3, 4, 8, 34])
print(my_list)
