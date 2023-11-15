import math
def sieve(limit):
    # sum of all primes up till some limit
    # find all primes till root of the limit
    primes = [True]*limit
    primes[0] = primes[1] = False
    for i in range(2, limit):
        for k in range(i+1, limit):
            if k % i == 0:
                #print(i, k)
                primes[k] = False
    return primes

limit = 2*10**6

primes = sieve(int(math.sqrt(limit))+1)

def checkprime(n):
    max = int(math.sqrt(n))+1
    for i in range(2, max):
        if primes[i] and n % i == 0:
            return False
    return True

sum = 0
for i in range(2, limit):
    if checkprime(i):
        #print(i)
        sum += i

print(sum)