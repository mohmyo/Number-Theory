def extendedgcd(p, r):
    x0, x1, y0, y1 = 1, 0, 0, 1
    while r != 0:
        q, p, r = p // r, r, p % r
        x0, x1 = x1, x0 - q * x1
        y0, y1 = y1, y0 - q * y1
    return p, x0, y0


# get a,b and m
a, b, m = map(int, input("\nEnter a,b and m to solve ax = b (mod m) \n").split())
# get x0,y0 and gcd of a and m
z, x, y = extendedgcd(a, m)
# if gcd(a,m) divides b then we have a solution
if b % z == 0:
    print("First, gcd(a=%s, m=%s) = %s" % (a, m, z))
    print("as %s divides %s then %sx = %s (mod %s) have exactly %s solutions" % (z, b, a, b, m, z))
    print("x0 = %s  as %s = %s·%s + %s·%s " % (x, z, x, a, y, m))
    print("b' = b/g = %s/%s = %s " % (b, z, b // z))
    print("m' = m/g = %s/%s = %s" % (m, z, m // z))
    print("and solutions are on form x',x'+m',...,x'+(g-1)m' so: ")
    print("x =", end=" ")
    # loop through x',x'+m',...,x'+(g-1)m' to get all solutions
    for i in range(z):
        print(((b // z * x) + i * (m // z)) % m, end="")
        if i != z - 1:
            print(",", end=" ")
    print(" mod %s" % m)
# gcd(a,m) does not divide b then there is no solutions
else:
    print("GCD of %s and %s is %s and %s doesn't divide %s" % (a, m, z, z, b))
    print("so linear congruence %sx = %s (mod %s) has no solutions" % (a, b, m))
