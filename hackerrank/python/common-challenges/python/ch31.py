# sWAP cASE

def swap_case(s):
    swaped = []

    for i in range(len(s)):
        if s[i].isupper():
            swaped.append(s[i].lower())
        else:
            swaped.append(s[i].upper())
    return ''.join(swaped)