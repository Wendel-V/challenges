def sockMerchant(n, ar):
    sock_types = list(set(ar))
    socks = {}
    for type in sock_types:
        count = 0
        for sock in ar:
            if type == sock:
                count += 1
        socks[type] = count
        count = 0
    for item in socks:
        if socks[item] <= 1:
            socks[item] = 0
        if socks[item] % 2 != 0:
            socks[item] -= 1
    return int(sum(socks.values()) / 2)