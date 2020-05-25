'''
direction => r = right, d = down
color => black == 1, white == 0
'''
def print_ant_path(k):

    col = 'w'
    dr = 'r'
    i = k
    j = k
    max_i = i
    max_j = j
    min_i = i
    min_j = j
    ant_path = [(col,dr,i,j)]
    while k > 0:
        if dr == 'r':
            if col == 'w':
                col = 'b'
                dr = 'd'
                i += 1
            else:
                col = 'w'
                dr = 'u'
                i -= 1
        elif dr == 'l':
            if col == 'w':
                col = 'b'
                dr = 'u'
                i -= 1
            else:
                col = 'w'
                dr = 'd'
                i +=1
        elif dr == 'u':
            if col == 'w':
                col = 'b'
                dr = 'r'
                j += 1
            else:
                col = 'w'
                dr = 'l'
                j -= 1
        elif dr == 'd':
            if col == 'w':
                col = 'b'
                dr = 'l'
                j -= 1
            else:
                col = 'w'
                dr = 'r'
                j += 1
        ant_path.append((col,dr, i, j))
        if max_i < i:
            max_i = i
        if max_j < j:
            max_j = j
        if min_i > i:
            min_i = i
        if min_j > j:
            min_j = j

        k -= 1
    print(ant_path)

print_ant_path(5)
