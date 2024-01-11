def pageCount(n, p):
    front_flip = p // 2
    back_flip = 0
    if n % 2 == 0:
        back_flip = (n - p + 1) // 2
    else:
        back_flip = (n - p) // 2
    return min(front_flip, back_flip)
