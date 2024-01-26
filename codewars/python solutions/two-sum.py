def two_sum(numbers, target):
    complement = {}

    for index, num in enumerate(numbers):
        if num in complement:
            return (complement[num], index)
        complement[target - num] = index

    return None
