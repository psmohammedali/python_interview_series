def print_n(num):
    if num == 1:
        print(num, end = " ")
        return
    print_n(num-1)
    print(num, end=" ")
    return


print_n(960)
