#Find the percentage

query = {
    'alpha':[20,30,40],
    'beta':[30,50,70]
}

result = round(sum(query['alpha']) / len(query['alpha']), 3)

print('{:.2f}'.format(result))