def find_index_x(my_list, num, cur_index):
    if cur_index == -1:
        return -1
    if my_list[cur_index] == num:
        return cur_index
    smallOutput = find_index_x(my_list, num, cur_index - 1)
    return smallOutput

def find_last_index_x_through_first(my_list, num, cur_index):
    if cur_index == len(my_list):
        return -1
    my_smaller_list_output = find_last_index_x_through_first(my_list,num,cur_index+1)
    if my_smaller_list_output == -1 and my_list[cur_index] == num:
        return cur_index
    return my_smaller_list_output


my_list = [1, 2, 8, 9, 7, 4, 1, 5]
print(find_last_index_x_through_first(my_list, 1, 0))
