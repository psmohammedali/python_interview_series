def list_sorted(my_list):
    if len(my_list) <= 1:
        return True
    small_list = my_list[0:len(my_list)-1]
    is_small_sorted = list_sorted(small_list)
    if is_small_sorted == True and small_list[-1] < my_list[-1]:
        return True
    else:
        return False


def list_sorted_opt(my_list, index):
    if index == len(my_list)-1 or index == len(my_list):
        return True
    # checking the first two eleemnt
    if my_list[index] > my_list[index+1]:
        return False
    mysmallOutput = list_sorted_opt(my_list,index+1)
    return mysmallOutput

print(list_sorted_opt([],0))