def gcd(p, q):
    if p < q:
        return gcd(q, p)
    if q == 0:
        return p
    return gcd(q, p % q)


def get_all_values_of_n(remainder):
    for i in range(m):
        if i % 2 == remainder:
            if gcd(i, m) == 1:
                n_list.append(i)


m = int(input("\nPlease Enter m\n"))
n_list = []

if m % 2 == 0:
    print("m is even, so get all values of n where n is odd and gcd(m,n)=1")
    get_all_values_of_n(remainder=1)
else:
    print("m is odd, so get all values of n where n is even and gcd(m,n)=1")
    get_all_values_of_n(remainder=0)

print("All values of n are %s" % n_list)
print("calculate x = m^2 - n^2 , y = 2mn , z = m^2 + n^2 for every n")
print("So all Primitive Pythagorean Triples with y even are :\n")

for n in n_list:
    print("at n = %s :" % n, end=" ")
    x = m ** 2 - n ** 2
    y = 2 * m * n
    z = m ** 2 + n ** 2
    print("(%s ,%s ,%s)" % (x, y, z))
