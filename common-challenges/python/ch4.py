def diagonalDifference(arr):
    diag_prim, diag_sec = [],[]
    i = 0
    j = 0

    row_size = len(arr[i])
    col_size = len(arr[j])

    while i < row_size:
        j = 0
        while j < col_size:
            if(i == j): diag_prim.append(arr[i][j])
            elif((i+j) == (row_size - 1)): diag_sec.append(arr[i][j])
            j += 1
        i += 1
    
    
    if((row_size % 2) != 0): diag_sec.append(diag_prim[len(diag_prim)//2]) 

    diff = sum(diag_prim) - sum(diag_sec)

    return abs(diff)