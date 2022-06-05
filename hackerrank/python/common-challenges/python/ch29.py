# Lists


if __name__ == '__main__':
    N = int(input())
    
result = []
for i in range(N):
    splited=input().strip().split(" ")
    if splited[0] == 'append':
        result.append(int(splited[1]))
    elif splited[0] == 'insert':
        result.insert(int(splited[1]), int(splited[2]))
    elif splited[0] == 'print':
        print(result)
    elif splited[0] == 'remove':
        result.remove(int(splited[1]))
    elif splited[0] == 'sort':
        result.sort()
    elif splited[0] == 'pop':
        result.pop()
    else:
        result = result[::-1]