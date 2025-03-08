# # no of columns are same
# rows = int(input())
#
# # taking input from the user - list comprehension
# two_d_list = [[int(col) for col in input().split(" ")] for row_num in range(rows)]
#
# col_size = len(two_d_list[0])
#
# largest_col_sum = -1
#
# for col_no in range(col_size):
#     current_col_sum = 0
#     for row_num in range(rows):
#         curr_cell = two_d_list[row_num][col_no]
#         current_col_sum += curr_cell
#     if largest_col_sum < current_col_sum:
#         largest_col_sum = current_col_sum
#
# print(largest_col_sum)

for i in range(5,-1,-1):
    print(i)