with open('q13input.txt') as f:
    lines = f.readlines()
for i in range(len(lines)):
    lines[i] = lines[i][:-1]
    lines[i] = lines[i].split()
    for j in range(len(lines[i])):
        lines[i][j] = int(lines[i][j])
sum = 0
for i in lines:
    sum += i[0]

sum = str(sum)[:10]
print(len(sum))
print(sum)