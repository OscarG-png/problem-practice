def countingValleys(steps, path):
    # Write your code here
    level = 0
    valleys = 0

    for step in path:
        if step == "U":
            level += 1
            if level == 0:
                valleys += 1
        else:
            level -= 1
    return valleys
