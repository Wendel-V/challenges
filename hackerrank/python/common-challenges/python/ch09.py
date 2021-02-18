def timeConversion(s):
    date = list(s)

    date.pop(len(date)-1)
    letter = date.pop(len(date)-1)


    if(letter == 'P' and date[0] == '1' and date[1] == '2'):
        result = ''.join(date)
    elif (letter == 'P'):
        new_hour = str(int(date[0]+date[1]) + 12)
        del(date[0:2])
        date.insert(0, new_hour)
    elif(letter == 'A' and date[0] == '1' and date[1] == '2'):
        new_hour = '00'
        del(date[0:2])
        date.insert(0, new_hour)

    result = ''.join(date)
    print(result)
    
 