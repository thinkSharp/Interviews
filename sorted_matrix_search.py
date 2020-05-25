def find_num_in_matrix(m, num):
    row_len = len(m)
    if row_len == 0:
        return -1
    col_len = len(m[0]) - 1
    i = 0
    j = col_len
    while True:
        if i == row_len or j == -1:
            return -1
        if m[i][j] == num:
            return i, j
        elif m[i][j] > num:
            j -= 1
        else:
            i += 1

print(find_num_in_matrix([[15,20,40,85],[20,35,80,95],[30,55,95,105],[40,80,100,120]],55))
print(find_num_in_matrix([[15,20,40,85],[20,35,80,93],[30,55,95,105],[40,80,100,120]],95))
