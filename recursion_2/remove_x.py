def remove_element(my_list, ele, curr_index, new_list):
    if curr_index == len(my_list):
        return
    if my_list[curr_index] != ele:
        new_list.append(my_list[curr_index])
    # calling my small brother who will take care of smaller list
    remove_element(my_list, ele, curr_index + 1, new_list)


my_list = [1, 2, 4, 5,5,5,5,5, 3, 6]
new_list = []
remove_element(my_list, 5, 0, new_list)
print(new_list)
