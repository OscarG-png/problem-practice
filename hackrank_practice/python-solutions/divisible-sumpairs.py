def divisibleSumPairs(n, k, ar):
    count = 0
    for i, a in enumerate(ar[:-1]):
        for b in ar[i + 1:]:
            if (a + b) % k == 0:
                count += 1
    return count
