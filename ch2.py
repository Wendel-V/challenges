def compareTriplets(a, b):
    ap = 0
    bp = 0
    re = []

    for i in list(range(3)):
        if a[i] > b[i]:
            ap += 1
        elif a[i] < b[i]:
            bp += 1

    re.append(ap)
    re.append(bp)

    return re
