def numTeams(rating):
    len_rating = len(rating)
    if len_rating == 0:
        return 0
    count = 0
    for i in range(len_rating):
        for j in range(i, len_rating):
            for k in range(j, len_rating):
                if rating[i] < rating[j] < rating[k]:
                    count +=1
                if rating[i] > rating[j] > rating[k]:
                    count +=1
    return count

def test_num_teams():
    count = numTeams([2,5,3,4,1])
    print(count)
test_num_teams()

