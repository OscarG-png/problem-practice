def pickingNumbers(a):
    element_count = {}

    for num in a:
        element_count[num] = element_count.get(num, 0) + 1

    max_length = 0

    for key in element_count:
        current_length = element_count[key] + element_count.get(key + 1, 0)
        max_length = max(max_length, current_length)

    return max_length
