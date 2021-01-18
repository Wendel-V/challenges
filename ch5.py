def plusMinus(arr):
    size = len(arr)
    positive = 0
    negative = 0
    zero = 0

    for element in arr:
        if element > 0:
            positive += 1
        elif element < 0:
            negative += 1
        else:
            zero += 1

    print('{0:.6f}'.format(positive/size))
    print('{0:.6f}'.format(negative/size))
    print('{0:.6f}'.format(zero/size))
