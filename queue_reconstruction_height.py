def reconstructQueue(people):
    """
    :type people: List[List[int]]
    :rtype: List[List[int]]
    Goal: reconstruct the queue based on hight and no of people in front of them
    based scenario: => no base
    recourance:
       double for loop:
        first loop will goes from i to len,
        second will go from i to 0
           and do the compare and swap
    """
    len_people = len(people)
    if len_people == 0:
        return people
    people = sorted(people, key=lambda x: (-x[0], x[1]))
    print(people)
    output = []
    for p in people:
        output.insert(p[1], p)
        print(output)
    return output


def test_queue_reconstruction():
    people = reconstructQueue([[7, 0], [4, 4], [7, 1], [5, 0], [6, 1], [5, 2]])
    print(people)
    people = reconstructQueue([[7, 1], [6, 1], [7, 0]])
    print(people)


test_queue_reconstruction()
