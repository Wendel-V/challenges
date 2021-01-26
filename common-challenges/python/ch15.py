def birthday(s, d, m):
    num_seg = len(s) - m + 1
    i = 0 
    j = m
    count = 0

    if (len(s) == 1) and s[0] == d:
        return count + 1

    for segment in range(num_seg):
        if j > len(s):
            break
        if sum(s[i:j]) == d:
            count += 1
        i += 1
        j += 1
    print(count)
