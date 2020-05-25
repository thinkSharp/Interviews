def sort_by_anagram(str_arr):
    def bubble_sort(arr):
        is_sorted = True
        while True:
            for i in range(1, len(arr)):
                if arr[i] < arr[i-1]:
                    temp = arr[i-1]
                    arr[i-1] = arr[i]
                    arr[i] = temp
                    is_sorted = False
            if is_sorted:
                return arr
            is_sorted = True

    def is_anagram(str1, str2):
        dict = {}
        for s in str1:
            if s == ' ':
                continue
            if s in dict:
                dict[s] += 1
            else:
                dict[s] = 1
        for s in str2:
            if s == ' ':
                continue
            if s in dict:
                dict[s] -= 1
            else:
                dict[s] = 1
        for k, v in dict.items():
            if v != 0:
                return False
        return True

    return sorted(str_arr, key=is_anagram())



