def breakingRecords(scores):
    max_count = 0
    current_max = scores[0]

    for score in scores:
        if score > current_max:
            current_max = score
            max_count += 1
    min_count = 0
    current_min = scores[0]

    for score in scores:
        if score < current_min:
            current_min = score
            min_count += 1
    return [max_count, min_count]


# problem wanted me to count the number of times
# the max and min scores were broken
