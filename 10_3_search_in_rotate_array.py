def binary_search(arr, item):
    def search_in_rotated_array(left, right):
        if left > right:
            return -1
        mid = (left + right) // 2
        if arr[mid] == item:
            return mid
        if arr[left] < arr[mid]:
            if arr[left] <= item < arr[mid]:
                return search_in_rotated_array(left, mid -1)
            else:
                return search_in_rotated_array(mid + 1, right)
        elif arr[mid] < arr[left]:
            if arr[mid] < item <= arr[right]:
                return search_in_rotated_array(mid + 1, right)
            else:
                return search_in_rotated_array(left, mid - 1)
        else:
            return search_in_rotated_array(left, mid - 1)
            if result == -1:
                return search_in_rotated_array(mid + 1, right)
    return search_in_rotated_array(0, len(arr)-1)

def test_binary_search():
    result = binary_search([15,16,19,20,25,1,3,4,5,7,10,14], 5)
    print(result)
    assert(result == 8)
    result = binary_search([15, 16, 19, 20, 25, 1, 3, 4, 5, 7, 10, 14], 19)
    print(result)
    assert (result == 2)
    result = binary_search([2,2,2,3,4,5,2], 2)
    print(result)
    assert (result == 1)


test_binary_search()
print(int(0x1F))