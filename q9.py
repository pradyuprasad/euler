for a in range(1, 1001):
    for b in range(a,1001):
        c = 1000-(a+b)
        if a**2 + b**2 == c**2:
            print(a, b, c)
            print("sum is", a+b+c)
            print("a^2 is", a**2)
            print("b^2 is", b**2)
            print("c^2 is", c**2)
