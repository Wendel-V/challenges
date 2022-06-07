#Alphabet Rangoli

def print_rangoli(size):
    import string    
    letters = list(string.ascii_lowercase[:size])
    altura = (size * 2) - 1
    largura = altura * 2 - 1
    letters = letters[::-1]

    for i in range(1, len(letters) + 1):
        a = '-'.join(letters[:i])
        b = a[::-1][1:]
        print((a+b).center(largura, '-'))

    for i in range(len(letters)-1, 0, -1):
        a = '-'.join(letters[:i])
        b = a[::-1][1:]
        print((a+b).center(largura, '-'))

