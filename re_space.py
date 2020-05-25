
def re_space(str_re_space, dic):
    len_str = len(str_re_space)

    def split(start, memo):
        if start >= len_str:
            return '', 0

        if len(memo[start]) > 0:
            return memo[start]

        best_invalid = len_str + 100
        parse = ''
        best_parse = ''
        for index in range(start, len_str):
            c = str_re_space[index]
            parse += c
            invalid = 0 if parse in dic else len(parse)
            print("Parse: {0}-{1} count {2}".format(parse, invalid, index))
            if invalid < best_invalid:
                result = split(index + 1, memo)
                if invalid + result[1] < best_invalid:
                    best_invalid = invalid + result[1]
                    best_parse = "{0} {1}".format(parse, result[0])
                    print("best_parse: {0} - {1}, invalid:{2}, best_pase:{3}".format(best_parse, index, invalid, best_invalid))

                    if best_invalid == 0:
                        break
        memo[start] = best_parse, best_invalid
        return memo[start]

    m = [''] * len_str
    return split(0, m)[0]


def test_re_space():
    result = re_space('thisis',set(['this', 'is', 'awesome']))
    print(result)

test_re_space()