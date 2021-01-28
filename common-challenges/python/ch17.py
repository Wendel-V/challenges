def migratoryBirds(arr):
    types = {1: 0, 2: 0, 3: 0, 4: 0, 5: 0 }
    for bird in arr:
        types[bird] += 1

    types_list_tuple = list(types.items())[::-1]
    max_num = 0
    list_tuple2 = []

    for i in types_list_tuple:
        if i[1] >= max_num:
            list_tuple2.append(i)
            max_num = i[1]

    max_num = 0
    max_element = list_tuple2[0]
    for a in list_tuple2:
        if max_num <= a[1]:
            max_num = a[1]
            max_element = a

    return max_element[0]