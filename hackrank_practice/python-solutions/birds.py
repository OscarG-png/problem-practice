def migratoryBirds(arr):
    bird_dict = {}

    for bird in arr:
        if bird in bird_dict:
            bird_dict[bird] += 1
        else:
            bird_dict[bird] = 1
    max_count = max(bird_dict.values())
    max_key = [key for key, value in bird_dict.items() if value == max_count]

    return min(max_key)
