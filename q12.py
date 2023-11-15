import math

divisors = {
    1: {1}
}

def find_divisors_memoized(n):
    if divisors.get(n) is not None:
        return divisors.get(n)
     
    divisors_n = {1, n}
    end = int(math.sqrt(n))+1
    for i in range(2, end):
        #print(i)
        if n % i == 0:
            divisor1 = i
            divisor2 = n//i
            divisors_n = divisors_n.union(find_divisors_memoized(divisor1), find_divisors_memoized(divisor2))
    divisors[n] = divisors_n

    return divisors_n 




def count_divisors(n):
    return len(find_divisors_memoized(n))

n = 1

def triangular(n):
    return int(n*(n+1)/2)

while (count_divisors(triangular(n)) < 500):
    #print(triangular(n), count_divisors(triangular(n)))
    n += 1

print(triangular(n))