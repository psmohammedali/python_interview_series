def sum_of_n(n):
    if n == 1:
        return 1
    small_ans = sum_of_n(n-1)
    my_ans = n + small_ans
    return my_ans


print(sum_of_n(4))

