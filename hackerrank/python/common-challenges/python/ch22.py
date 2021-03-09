def countingValleys(steps, path):
    valleys, level, list_level = 0, 0, [0]
    for i in path:
        if i == 'U':
            level += 1
            list_level.append(level)
        else:
            level -= 1
            list_level.append(level)
    list_level.pop(-1)
    for i in range(steps):
        if list_level[i] == 0:
            if list_level[i+1] < 0:
                valleys +=1
    return valleys

countingValleys(8, 'UDDDUDUU')