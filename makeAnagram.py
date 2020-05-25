
def isAnagram(s1, s2):
    if s1 == s2:
        return False
    lst1 = [0] * 123
    lst2 = [0] * 123
    for w in s1:
        lst1[ord(w)] += 1
    for w in s2:
        lst2[ord(w)] += 1
    delete_count = 0
    match_count = 0
    for i in range(ord('a'), ord('z') +1):
        if lst1[i] != lst2[i]:
            delete_count += abs(lst1[i] - lst2[i])
        elif lst1[i] == lst2[i] and lst1[i] != 0:
            match_count += 1
    if match_count > 0 and delete_count == 0 and s1 != s2:
        return 0
    elif match_count > 0 and delete_count > 0:
        return delete_count
    return delete_count

print(isAnagram('cde', 'abc'))