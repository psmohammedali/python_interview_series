# facorial function using recursion

def recur_function(n):
    if n == 0:
        return 1
    small_recur_function = recur_function(n - 1)
    my_ans = n * small_recur_function
    return my_ans


print(recur_function(3))
