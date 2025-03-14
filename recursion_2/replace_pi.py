def repalce_pi(my_str):
    if len(my_str) == 1 or len(my_str) == 0:
        return my_str
    if my_str[0]+my_str[1] == "pi":
        my_small_output = repalce_pi(my_str[2:])
        return str(3.14) + my_small_output
    smallOutput = repalce_pi(my_str[1:])
    return my_str[0] + smallOutput


my_str = "abpide"
print(repalce_pi(my_str))