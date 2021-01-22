x = [1,2,3,4,5]

def miniMaxSum(arr):

    result = []
    aux = 0

    for i in range(5):
        i = arr.copy()
        del(i[aux])
        result.append(sum(i))
        aux += 1
    
    print(str(min(result)) + ' ' + str(max(result)))

miniMaxSum(x)
