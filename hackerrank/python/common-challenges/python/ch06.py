def staircase(n):
    sharp = n

    for jump in range(n):

        aux = 1
        row = ''

        for element in range(n):
            if(aux < sharp): 
                row = row + ' '
            else:
                row = row + '#'
            aux += 1

        sharp -= 1

        print(row)
    