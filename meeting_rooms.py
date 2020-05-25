import collections
import heapq

def minMeetingRooms(intervals):
    """
    :type intervals: List[List[int]]
    :rtype: int
    goal: find the time overlap so that we can identify the no or rooms required
    based:
       sort the intervals so that we can make
    recourance:
       check to see the new interval start time is greater then any of the existing end time
    """
    if len(intervals) == 0:
        return 0

    intervals = sorted(intervals)
    rooms_count = 0
    rooms = []
    for start_time, end_time in intervals:
        len_room = len(rooms)

        if len_room == 0:
            rooms.append(end_time)
        elif rooms[-1] <= start_time:
            while rooms:
                item = rooms[-1]
                if item <= start_time:
                    rooms.remove(item)
                else:
                    break
            rooms.append(end_time)
        elif rooms[0] <= start_time:
            while rooms:
                item = rooms[0]
                if item <= start_time:
                    rooms.remove(item)
                else:
                    break
            rooms.append(end_time)
        else:
            rooms.append(end_time)
        rooms.sort()
        len_room = len(rooms)
        if rooms_count < len_room:
            rooms_count = len_room

    return rooms_count

def minMeetingRooms2(intervals):
    if len(intervals) == 0:
        return 0
    intervals = sorted(intervals)
    print(intervals)
    rooms = [intervals[0][1]]
    room_num = 1
    for i in range(1, len(intervals)):

        while len(rooms) > 0 and rooms[0] <= intervals[i][0]:
            heapq.heappop(rooms)
        heapq.heappush(rooms,intervals[i][1])
        print("i:{0} =>{1}".format(i,rooms))
        if room_num < len(rooms):
            room_num = len(rooms)
    return len(rooms)

def test_meeting_rooms():
    result = minMeetingRooms2([[13,15],[1,13],[6,9]])
    print(result)
    result = minMeetingRooms2([[928,5032],[3072,3741],[3960,4588],[482,2269],[2030,4360],[150,772]])
    print(result)
    result = minMeetingRooms2([[11,20],[4,19],[13,17],[6,13]])
    print(result)
    result = minMeetingRooms2([[7, 10], [2, 4],[3,5]])
    print(result)
    result = minMeetingRooms2([[0,30],[5,10],[15,20]])
    print(result)

test_meeting_rooms()