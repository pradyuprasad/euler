collatz_memo = {
    1:1
    
}

def collatz_m(n):
    if n in collatz_memo:
        return collatz_memo.get(n)
    if n % 2 == 0:
        C = 1 + collatz_m(n//2)
        collatz_memo[n] = C
        return C
    else:
        C = 1 + collatz_m(3*n+1)
        collatz_memo[n] = C
        return C
    
for i in range(1, 1000000):
    print(i)
    collatz_m(i)

largest = max(collatz_memo, key = collatz_memo.get)
print(largest)