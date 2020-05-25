def string_pattern_matching(value, pattern):
    def pattern_word_count(ptn):
        first = 0
        second_pos = 0
        fst_word = 'a' if ptn[0] == 'a' else 'b'
        for i in range(0, len(ptn)):
            if ptn[i] == fst_word:
                first += 1
            elif second_pos == 0:
                second_pos = i
        return fst_word, first, second_pos, len(ptn) - first

    def build_pattern_string(f_word, fst, snd):
        ptn_lst = []
        for i in range(0, len(pattern)):
            if pattern[i] == f_word:
                ptn_lst.append(fst)
            else:
                ptn_lst.append(snd)
        return ''.join(ptn_lst)

    first_pattern, f_count, s_position, s_count = pattern_word_count(pattern)
    str_len = len(value)
    max_f_len = str_len // f_count
    for f_size in range(1, max_f_len + 1):
        first_word = value[0:f_size]
        remaining_size = str_len - (f_size * f_count)
        second_position = s_position * f_size
        if s_count > 0 and remaining_size > 0 and second_position < str_len:
            sec_index = remaining_size // s_count
            sec_word = value[second_position: second_position + sec_index]
            pattern_str = build_pattern_string(first_pattern, first_word, sec_word)
            print("fst:" + first_word + ", sec:" + sec_word + " ptn: " + pattern_str)
            if pattern_str == value:
                return True
        else:
            pattern_str = build_pattern_string(first_pattern, first_word, '')
            if pattern_str == value:
                return True
    return False


def test_string_pattern_match():
    result = string_pattern_matching("catcatgocatgo", "aabab")
    print(result)

    result = string_pattern_matching("catcatgocatgoa", "aabab")
    print(result)

    result = string_pattern_matching("catcatcatcat", "aaaa")
    print(result)
    assert not result


test_string_pattern_match()
