def xml_encoding(element, attributes):
    def split_by_key_word(wd, key):
        split_wd = wd.split(key)

    tags = {}
    tags['<'] = '1'
    tags['>'] = '0'
    tags['</'] = '2'
    tag_count = 3
    for attribute in attributes:
        tags[attribute] = str(tag_count)
        tag_count += 1

    words = element.split()
    encoded_msg = []
    for w in words:
        split_wd = w.split('><')
        wds = [w]
        if len(split_wd) > 1:
            split_wd[0] = split_wd[0] + '>'
            split_wd[1] = '<' + split_wd[1]
            wds = split_wd
        for word in wds:
            len_w = len(word)
            if len_w == 0:
                continue
            if len_w >= 2 and word[0:2] == '</':
                encoded_msg.append(tags['</'])
                word = word[2:]

            splits = word.split('=')
            for wd in splits:
                if len(wd) > 1:
                    if wd[0] == '<':
                        encoded_msg.append(tags['<'])
                        wd = wd[1:]
                    elif wd[-1] == '>':
                        encoded_msg.append(tags['>'])
                        wd = wd[0:-1]
                if wd in tags:
                    encoded_msg.append(tags[wd])
                else:
                    encoded_msg.append(wd)
    return ' '.join(encoded_msg), tags

def test_xml_encoding():
    result = xml_encoding("<family lastName='McDowell' state='CA'><person firstName='Gayle'> Some Message </person></family>", ['family', 'person', 'firstName', 'lastName', 'state'])
    print(result[0])

test_xml_encoding()


