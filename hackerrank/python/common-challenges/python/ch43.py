# the Minion Game

string = 'BAANANAS'
vowels = 'AEIOU'   
kevin = 0
slen = len(string)
tsubs = ((slen * (slen + 1)) / 2)   

while string != '':
        for i in range(0,len(string)+1):
                if string[:i] != '':
                        if string[:i][0] in vowels:
                                kevin+= 1
        string = string[1:]

stuart = slen - kevin
           
if stuart > kevin:
        print('Stuart', stuart)
elif stuart < kevin:
        print('Kevin', kevin)
else:
        print('Draw')



string = 'BANANA'
slen = len(string)
tsubs = (slen * (slen + 1) )/2
vowels = 'AEIOU'

kevin = sum([slen - i for i in range(len(string)) if string[i] in vowels])

stuart = tsubs - kevin

if stuart > kevin: print('Stuart', int(stuart))
elif stuart < kevin: print('Kevin', (kevin))
else:print('Draw')
