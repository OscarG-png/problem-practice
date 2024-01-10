def birthday(s, d, m):
    cuts = 0
    for i in range(len(s) - m + 1):
        section = s[i:i + m]
        if sum(section) == d:
            cuts += 1
    return cuts


# I  needed to find a section that adds up to the users birthday
# with a length equal to their birth month
