def sockMerchant(n, ar):
    sock_dict = {}
    for sock in ar:
        if sock in sock_dict:
            sock_dict[sock] += 1
        else:
            sock_dict[sock] = 1
    pair_count = 0
    for key, value in sock_dict.items():
        if value >= 2:
            pair_count += value // 2
    return pair_count
