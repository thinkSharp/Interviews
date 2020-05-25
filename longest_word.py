def build_longest_word(lst):
    def find_longest(map_lst, word, is_original):
        if word in map_lst and not is_original:
            return map_lst[word]
        for i in range(0,len(word)):
            left = word[0:i]
            right = word[i:]
            print("i: {0}, left: {1}, right:{2}".format(i, left, right))
            if left in map_lst and map_lst[left] and find_longest(map_lst, right, False):
                return True
        map_lst[word] = False
        return False

    lst_map = {}
    for item in lst:
        lst_map[item] = True
    lst = sorted(lst, key=len, reverse=True)
    for item in lst:
        result = find_longest(lst_map, item, True)
        if result:
            return item
    return None


def test_longest_word():
    result = build_longest_word(['a', 'zz', 'wbc', 'ibelieveicanfly', 'touchtheskybelieve','touch', 'the','fly','sky', 'i', 'believe', 'can'])
    print(result)

test_longest_word()