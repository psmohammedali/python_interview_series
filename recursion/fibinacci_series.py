def fibbi(n):
    if n == 1:
        return 1
    if n == 0:
        return 0
    fibbi_n_1 = fibbi(n-1)
    fibbi_n_2 = fibbi(n-2)
    my_fibbi = fibbi_n_1 + fibbi_n_2
    return my_fibbi


print(fibbi(6))