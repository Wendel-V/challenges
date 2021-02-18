def kangaroo(x1, v1, x2, v2):

    if x1 > x2 and v2 > v1:
        if(x1 - x2) % (v2 - v1) == 0:
            return 'YES'
        else:
            return 'NO'
    elif x1 < x2 and v2 < v1:
        if(x1 - x2) % (v2 - v1) == 0:
            return 'YES'
        else:
            return 'NO'
    else: return 'NO'    

