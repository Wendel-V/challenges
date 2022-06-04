# list comprehensions

x = 1
y = 1
z = 2
n = 3

xlen = len(range(0,x+1))
ylen = len(range(0, y+1))
zlen = len(range(0, z+1))

print([[x, y, z] for x in range(xlen) for y in range(ylen) for z in range(zlen) if x + y + z != n])