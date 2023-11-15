a, b = 0, 1

def count_length(n):
    return len(str(n))

counter = 1
while (count_length(b) < 1000):
    counter += 1
    a, b = b, a + b

print(counter)