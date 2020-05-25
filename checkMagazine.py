def checkMagazine(lst_words, lst_node):
    words = {}

    for i in range(0, len(lst_words)):
        if lst_words[i] in words:
            words[lst_words[i]] += 1
        else:
            words[lst_words[i]] = 1

    for i in range(0, len(lst_node)):
        if not lst_node[i] in words:
           print("No")
           return "No"
        else:
            words[lst_node[i]] -=1
            if (words[lst_node[i]] == 0):
                del words[lst_node[i]]
    print("Yes")
    return "Yes"

def test():
    result = checkMagazine(['apgo', 'clm', 'w', 'lxkvg', 'mwz', 'elo', 'bg', 'elo', 'lxkvg', 'elo', 'apgo', 'apgo', 'w', 'elo', 'bg'],['elo', 'lxkvg', 'bg', 'mwz', 'clm', 'w'])
    print(result)
    assert(result == "Yes")
    result = checkMagazine(['give', 'me', 'one', 'grand', 'today', 'night'], ['give', 'one', 'grand', 'today'])
    print(result)
    assert(result == "Yes")
    #result = checkMagazine("two times three is not four","two times two is four")
    #print(result)
    #assert (result == "No")
    #result = checkMagazine("ive got a lovely bunch of coconuts", "ive got some coconuts")
    #print(result)
    #assert(result == "No")

test()
