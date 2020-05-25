def find_duplicate(input, input_size):
    def get_bit(local_arr, pos):
        byte_pos = pos // 32
        bit_pos = pos % 32
        return local_arr[byte_pos] & (1 << bit_pos)

    def set_bit(local_arr, pos):
        byte_pos = pos >> 5 # right shift 5 means divide by 32 = 2 ^ 5
        bit_pos = pos & 0x1F # 0x1F == 31 since modulus of pos % 32 can only be 0 to 31
        local_arr[byte_pos] |= (1 << bit_pos)

    arr = [0] * (input_size// 32)
    for i in input:
        i = i - 1  # index is zero size
        if get_bit(arr, i):
            print(i + 1, end= ',')
        else:
            set_bit(arr, i)
    print("")
def test_find_duplicate():
    find_duplicate([1,2,3,4,5,6,7,8,9,0,1,2,3,4,5,6,7,8,9,10,11,2,3,4,5,5,6,7,8,10,1,2], 32)

test_find_duplicate()