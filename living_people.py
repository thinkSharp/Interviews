def max_living_year(people):
    len_people = len(people)
    if len_people == 0:
        return 0, 0

    all_years = [0] * 2002

    for item in people:
        p, b, d = item
        if b < 1900 or b > 2000:
            continue
        if d < 1900 or d > 2000:
            continue
        all_years[b] += p
        all_years[d+1] -= p

    max_year = 0
    max_people = 0
    total = 0
    for i in range(1900, len(all_years)):
        total += all_years[i]
        if max_people < total:
            max_people = total
            max_year = i
    return max_people, max_year

def test_max_people():
    result = max_living_year([(5,1900,1980), (3,1902,1957), (5,1905,1940), (7,1950, 2000), (1, 1900, 2000)])
    print(result)

test_max_people()


