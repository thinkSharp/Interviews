def isPalindrome(input, ignore_white=True):
    len_str = len(input)

    word_dict = {}

    for l in input.lower():
        if l in word_dict:
            word_dict[l] += 1
        else:
            word_dict[l] = 1

    odd_count = 0
    white_count = 0
    for k, v in word_dict.items():
        if k == ' ' and ignore_white:
            white_count += 1
            continue
        r = v % 2
        if r != 0:
            odd_count += 1
    have_single = (len_str - white_count) % 2 != 0
    if (have_single and odd_count == 1) or (not have_single and odd_count == 0):
        return True
    return False


print(isPalindrome('Tact Coa'))
print(isPalindrome('bbc'))
print(isPalindrome('b b c '))
print(isPalindrome('b b c a'))
print(isPalindrome('tactcoapapa'))