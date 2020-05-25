def volume_of_histogram(heights):
    len_height = len(heights)
    left_max = [0] * len_height
    right_max = [0] * len_height
    volumes = [0] * len_height
    current_max = 0
    for i in range(len_height-1, -1, -1):
        max_height = heights[i]
        if current_max < max_height:
            current_max = max_height
        right_max[i] = current_max
    current_max = 0

    total_volumes = 0
    max_volumes = 0
    volumes_group = []
    for i in range(0, len_height):
        max_height = heights[i]
        if current_max < max_height:
            current_max = max_height
        left_max[i] = current_max
        volumes[i] = min(left_max[i], right_max[i]) - heights[i]
        total_volumes += volumes[i]
        if volumes[i] == 0:
            volumes_group.append(max_volumes)
            max_volumes = 0
        max_volumes += volumes[i]
    return total_volumes, volumes_group


def test_histogram_volume():
    heights = [0,0,4,0,0,6,0,0,3,0,5,0,1,0,0]
    result = volume_of_histogram(heights)
    print(result)

test_histogram_volume()