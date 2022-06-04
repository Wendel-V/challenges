#Nested Lists

records = [['harsh', 20],['Beria', 20],['Varun',19],['Kakunami',19],['Vikas',21]]

if __name__ == '__main__':
    records = []
    for _ in range(int(input())):
        name = input()
        score = float(input())
        records.append([name,score])

minlist = []
min = records[0]

for i in records:
    if i[1] < min[1]:
        min = i
        minlist = [min]
    elif i[1] == min[1]:
        minlist.append(i)

for i in minlist:
    records.remove(i)

minlist = []

min = records[0]

for i in records:
    if i[1] < min[1]:
        min = i
        minlist = [min]
    elif i[1] == min[1]:
        minlist.append(i)

minlist.sort()
for i in minlist:
    print(i[0])
        