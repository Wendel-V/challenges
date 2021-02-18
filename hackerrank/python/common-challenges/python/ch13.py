from math import gcd

def findgcd(x, y):
   while(y):
      x, y = y, x % y
   return x

def factors(initial, finish, factor):
    result = []
    if initial == 1:
        result.append(initial)
        initial +=1
    while initial <= finish:
        if initial % factor == 0:
            result.append(initial)
        initial += 1
    return result

def lcmOfArray(a):
    if len(a) < 2:
        return a[0]
    lcm = a[0]
    for i in a[1:]:
        lcm = lcm*i//findgcd(lcm, i)
    return lcm     

def gcdOfArray(b):
    if len(b) < 2:
        return b[0]
    num1=b[0]
    num2=b[1]
    result = findgcd(num1,num2)
    for i in range(2,len(b)):
        result = findgcd(result,b[i])
    return result

def multiples(a, b):
    lcm_ = lcmOfArray(a)
    gcd_ = gcdOfArray(b)
    return list(factors(lcm_, gcd_, lcm_))

def getTotalX(a, b):
    multiples_list = multiples(a, b)
    gcd_ = gcdOfArray(b)
    count = 0
    if not multiples_list:
        return 0
    for item in multiples_list:
        if gcd_ % item == 0:
            count += 1
    return count
