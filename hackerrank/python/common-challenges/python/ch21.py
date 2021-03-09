def pageCount(n, p):
    i, f, count1, count2 = 1, n, 0, 0
    if p % 2 == 0:
        face = (p, p+1)
    else: 
        face = (p-1, p)
    while i < face[1]:
        i += 2
        count1 += 1
    while f > face[1]:
        f -= 2
        count2 += 1
    return min((count1, count2))


pageCount(5,4)
