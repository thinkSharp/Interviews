import collections
def alienOrder(words):
    """
    :type words: List[str]
    :rtype: str
    goal: get the order of letters
    steps:
        map these letters into parent->child relationship
        since these are in alian dictionary words, they are in alphabetical order
        we will create two dictionary, first one will tell us the relationship between letters
        second one will tell us parents count for each letter
        then we will use BFS to list all letters who do not have parents until that list is empty
    """
    len_words = len(words)
    if len_words == 0:
        return ""

    rel = {}
    p_count = {}

    word1 = words[0]
    for w in range(1, len_words):
        word2 = words[w]
        i , j = 0, 0
        len_iw, len_jw = len(word1), len(word2)
        while i < len_iw and j < len_jw:
            if word1[i] == word2[j]:
                i += 1
                j += 1
            else:
                if word1[i] not in rel:
                    rel[word1[i]] = []
                rel[word1[i]].append(word2[j])

                if word2[j] not in p_count:
                    p_count[word2[j]] = 0
                p_count[word2[j]] += 1

                if word1[i] not in p_count:
                    p_count[word1[i]] = 0

                word1 = word2
                break

    print(rel)
    print(p_count)
    queue = collections.deque()
    word_order = []
    visited = set()
    for k, v in p_count.items():
        if v == 0:
            queue.append(k)

    while queue:
        p = queue.popleft()

        if p in visited:
            continue

        visited.add(p)

        word_order.append(p)

        del p_count[p]

        if p in rel:
            cs = rel[p]
            for c in cs:
                if c in p_count:
                    p_count[c] -= 1

        for k, v in p_count.items():
            if v == 0 and k not in visited:
                queue.append(k)

    return ''.join(word_order)


def test_alian_dictionary():
    result = alienOrder(["z","z"])
    print(result)

test_alian_dictionary()

# for num in range(10,20):  #to iterate between 10 to 20
#    i = 2
#    while i < num:
#    #for i in range(2,num): #to iterate on the factors of the number
#       if num%i == 0:      #to determine the first factor
#          j=num/i #to calculate the second factor
#          print ('%d equals %d * %d' % (num,i,j))
#          break #to move to the next number, the #first FOR
#       i += 1
#    else:        # else part of the loop
#       print (num, 'is a prime number')

x = [(4, 1), (1, 2), (6, 0)]
print(x)
print(min(x, key=lambda n: n[0]))