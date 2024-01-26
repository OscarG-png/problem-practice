def find_it(seq):
    int_map = {}

    for num in seq:
        if num not in int_map:
            int_map[num] = 0
        int_map[num] += 1

    for key, value in int_map.items():
        if value % 2 != 0:
            return key
    return None


# find the number that occurs an odd amount of times
