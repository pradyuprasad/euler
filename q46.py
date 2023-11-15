import math
primes = []
def make_sieve(limit):
    global primes
    primes = [True]*limit
    primes[0] = primes[1] = False
    end = int(math.sqrt(limit))+1
    for i in range(2, limit):
        if primes[i]:
            for j in range(i+1, limit):
                if j % i == 0:
                    primes[j] = False

def extend_primes(newlimit):
    global primes
    if newlimit > len(primes):
        primes += [True] * (newlimit - len(primes))
        for i in range(2, newlimit):
            if primes[i]:
                for j in range(i+1, newlimit):
                    if j % i == 0:
                        primes[j] = False
    


def allprimesbelow(n):
    if n > len(primes):
        extend_primes(n+1)
    output = []
    for i in range(2, n):
        if primes[i]:
            output.append(i)
    return output

def check_composite(n):
    if n > len(primes):
        extend_primes(n+1)
    return not primes[n]

def check_perfectsquare(n):
    return (n ** 0.5).is_integer()

def checkgoldbach(n):
    primes_below = allprimesbelow(n)
    mapped = list(map(lambda x:(n-x)/2, primes_below))
    if len(list(filter(check_perfectsquare, mapped))) > 0:
        return True
    else: 
        return False
    

i = 33
'''while True:
    print("checking ", i)
    if (check_composite(i) and not checkgoldbach(i)):
        print(i, "passes")
        break
    else:
        i = i + 2'''

print(check_composite(5777) and not checkgoldbach(5777))


 