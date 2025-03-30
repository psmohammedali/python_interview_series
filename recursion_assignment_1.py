def geometric_sum(num):
    if num == 0:
        return 1
    small_geometric_sum = geometric_sum(num-1)
    my_value = round(1/pow(2,num),5)
    my_sum = small_geometric_sum + my_value
    return my_sum


num = 3
print(geometric_sum(num))
