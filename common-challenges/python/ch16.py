def divisibleSumPairs(n, k, ar):
    second = ar.copy()
    num = 1
    pair_num, iterator = 0, 0
    for i in ar:
        for j in second:
            if(num >= len(second)):
                break
            if ((i + second[num]) % k) == 0:
                pair_num += 1
            num += 1
        iterator += 1
        num = iterator + 1
    return pair_num
            
