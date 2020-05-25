def highestPopulation(people):
    birth, death = list(zip(*people))

    min_birth = min(birth)
    max_death = max(death) + 2
    people_arr = [0] * max_death

    for p in people:
        b, d = p
        if b in people_arr:
            people_arr[b] += 1
        else:
            people_arr[b] = 1

        if d in people_arr:
            people_arr[d + 1] -= 1
        else:
            people_arr[d + 1] = -1
    highest = 0
    highest_year = 0
    running_total = 0
    for i in range(min_birth, max_death):
        running_total += people_arr[i]
        if highest < running_total:
            highest = running_total
            highest_year = i

    return highest, highest_year


print(highestPopulation([(1900, 1930), (2000, 2020), (1980, 2020), (1950, 2010), (1970, 2015)]))
