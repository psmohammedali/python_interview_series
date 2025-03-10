def pow_n(base, power):
    if power == 1:
        return base
    small_power_ans = pow_n(base,power-1)
    my_ans = small_power_ans * base
    return my_ans


print(pow_n(2,10))