def is_valid_walk(walk):
    if len(walk) != 10:
        return False
    directions = {
        "n": 0,
        "s": 0,
        "w": 0,
        "e": 0
    }
    for char in walk:
        directions[char] += 1

    return directions["n"] == directions['s'] and directions['w'] == directions['e']
