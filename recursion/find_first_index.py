def find_index_x(my_list, num, cur_index):
    if cur_index == len(my_list):
        return -1
    if my_list[cur_index] == num:
        return cur_index
    smallOutput = find_index_x(my_list,num, cur_index+1)
    return smallOutput



print(find_index_x([],11,0))