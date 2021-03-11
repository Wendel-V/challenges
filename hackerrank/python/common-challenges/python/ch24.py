def catAndMouse(x, y, z):
    dist_a = abs(z - x)
    dist_b = abs(z - y)
    if dist_a < dist_b:
        return 'Cat A'
    elif dist_a > dist_b:
        return 'Cat B'
    else:
        return 'Mouse C'

print(catAndMouse(2,5,4))
print(catAndMouse(1,2,3))
print(catAndMouse(1,3,2))