def countApplesAndOranges(s, t, a, b, apples, oranges):
    n_apple, n_orange = 0, 0
    house = range(s,(t+1))
    apples_fell, oranges_fell = [],[]

    for apple in apples:
        apples_fell.append(apple + int(a))
    for orange in oranges:
        oranges_fell.append(orange + int(b))
    for apple in apples_fell:
        if(apple in house):
            n_apple += 1
    for orange in oranges_fell:
        if(orange in house):
            n_orange += 1
            
    print(n_apple)
    print(n_orange)


    countApplesAndOranges(7,11,5,15,[-2,2,1],[5,-6, -6])