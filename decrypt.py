'''
Encryption rule:
1) convert everything to ascii value
2) add one to first character
3) add previous character from second to last
4) subtract 26 till it reaches between ascii a-z
'''


def decrypt(word):

    lst_word = [c for c in word]
    decrypt_word = [''] * len(lst_word)
    start = ord(lst_word[0])
    decrypt_word[0] = chr(start - 1)
    for i in range(1, len(word)):
        ascii_val = ord(lst_word[i])
        diff = ascii_val - start
        while diff < 97:
            diff += 26
        decrypt_word[i] = chr(diff)
        start = ascii_val
    return ''.join(decrypt_word)


def test_decrypt():
    result = decrypt('dnotq')
    print(result)
    assert(result == 'crime')

    result = decrypt('flgxswdliefy')
    print(result)
    assert(result == 'encyclopedia')


test_decrypt()

