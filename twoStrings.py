def twoStrings(s1, s2):
    d = {}
    for i in s1:
        d[i] = 1
    for j in s2:
        if j in d:
            return "YES"
    return "NO"

def alternatingCharacters(s):
    count = 0
    for i in range(1, len(s)):
        if s[i-1] == s[i]:
            count +=1
    return count


print(alternatingCharacters('AAAA'))

def isValid(s):
    d = {}
    one_pass = False
    max_count = 0
    for i in s:
        if i in d:
            d[i] += 1
        else:
            d[i] = 1
    d2 = {}
    for i, value in d.items():
        if value in d2:
            d2[value] += 1
        else:
            d2[value] = 1
    fst_value = 0
    snd_value = 0
    fst_key = 0
    snd_key = 0
    key_value_one = False
    for i, value in d2.items():
        if (i == value) and (i == 1):
            key_value_one = True
        if value == 1:
            one_pass = True
        max_count += 1
        if fst_value == 0: fst_value = i
        else: snd_value = i
        if fst_key == 0 : fst_key = value
        else: snd_key = value
    print ("max_count:" + str(max_count) + " one_pass: " + str(one_pass) + " fst:" + str(fst_value) + ", " + str(fst_key) + " snd: " + str(snd_value) + ", " + str(snd_key))
    if max_count == 1 or (max_count == 2 and (one_pass and (abs(fst_value - snd_value) == 1) or key_value_one)) : return "YES"

    return "NO"





print(isValid('aaaaabc'))
print(isValid('aabbcd'))
