def find_multiples(integer, limit):
    result = []

    for i in range(integer, limit + 1, integer):
        result.append(i)
    return result
