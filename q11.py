with open('q11input.txt') as f:
    lines = f.readlines()
for i in range(len(lines)):
    lines[i] = lines[i][:-1]
    lines[i] = lines[i].split()
    for j in range(len(lines[i])):
        lines[i][j] = int(lines[i][j])
#print(lines)

M = lines

def right4(i, j):
    if i > 16:
        return 1
    product = 1
    for k in range(0,4):
        product *= M[i+k][j]
    return product

def left4(i, j):
    if i < 3:
        return 1
    product = 1
    for k in range(0,4):
        product *= M[i-k][j]
    return product

def top4(i, j):
    if j < 3:
        return 1
    product = 1
    for k in range(0, 4):
        product *= M[i][j-k]
    return product

def bottom(i, j):
    if j > 16:
        return 1
    product = 1
    for k in range(0, 4):
        product *= M[i][j+k]
    return product

def bottom_right(i, j):
    if i < 3 or i > 16 or j < 3 or j > 16:
        return 1
    product = 1
    for k in range(0, 4):
        product *= M[i+k][j+k]
    return product

def bottom_left(i, j):
    if i < 3 or i > 16 or j < 3 or j > 16:
        return 1
    product = 1
    for k in range(0, 4):
        product *= M[i-k][j+k]
    return product

largest = 1
for i in range(0, 19):
    for j in range(0, j):
        current_largest = max(bottom_right(i,j), bottom_left(i,j), bottom(i, j), top4(i, j), right4(i, j), left4(i,j))
        if current_largest > largest:
            largest = current_largest

print(largest)
