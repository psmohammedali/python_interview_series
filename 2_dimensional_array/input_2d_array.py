# taking input from the user
# 2
# 1 2 3 4
# 5 6 7 8

rows = int(input())
# for loop

# new_2d_list = []
# for row_n in range(rows):
#     row_input = input().split(" ")
#     integer_row = []
#     for i in row_input:
#         integer_row.append(int(i))
#     new_2d_list.append(integer_row)
#
# print(new_2d_list)


new_2d_list = [[int(char) for char in input().split()] for row_num in range(rows)]
print(new_2d_list)

# printing 2 d list
for row in new_2d_list:
    for col in row:
        print(col, end=" ")
    print()
