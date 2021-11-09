def utopianTree(n):
    height = 0
    for cycle in range(0,n+1):
        if (cycle % 2 == 1):
            height = height * 2
        elif (cycle % 2 == 0):
            height += 1
    return height
