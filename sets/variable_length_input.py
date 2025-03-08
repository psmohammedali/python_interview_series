def sum(a,b,*more_var):
    ans = 0
    for i in more_var:
        ans += i
    return ans + a + b

print(sum(1,2,1,2,1,2,11,2,1,1,1,21,1,2,2,))