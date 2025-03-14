def string_replace(my_str,old,new,curr_index):
    # It reached the end of the string
    if curr_index == len(my_str):
        return ""
    my_small_string = string_replace(my_str,old, new, curr_index+1)
    if my_str[curr_index] == old:
        return new + my_small_string
    else:
        return my_str[curr_index] + my_small_string

def string_replace_copy(my_str, old,new):
    if len(my_str) == 0:
        return ""
    my_small_string = string_replace_copy(my_str[1:],old,new)
    if my_str[0] == old:
        return new + my_small_string
    else:
        return my_str[0] + my_small_string


my_str = "bhavana mohanan"
print(string_replace_copy(my_str,"a","e"))