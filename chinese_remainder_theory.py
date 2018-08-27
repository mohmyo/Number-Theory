import sys


def gcd(p, q):
    if p < q:
        return gcd(q, p)
    if q == 0:
        return p
    return gcd(q, p % q)


def inverse(n, f):
    phi = phi_function(f)
    return int(n ** (phi - 1)) % f


def phi_function(k):
    num_coprime = 0
    for w in range(1, k):
        if gcd(w, k) == 1:
            num_coprime += 1
    return num_coprime


num_eqns = int(input("\nHow many equations you want to solve\n"))
a_list, m_list, n_list, h_list = [], [], [], []
M = 1
for i in range(num_eqns):
    a, m = map(int, input("please enter a%s and m%s\n" % (i + 1, i + 1)).split())
    a_list.append(a)
    m_list.append(m)
text_to_print = 'm1'
# check if m1,m2,...mt are pairwise relatively prime
for j in range(len(m_list) - 1):
    if j != 0:
        text_to_print += '· m%s' % (j + 1)
    M *= m_list[j]
    for i in range(len(m_list) - 1):
        if i != j:
            z = gcd(m_list[j], m_list[i])
            # if current pair not relatively prime
            if z > 1:
                print("Can't apply CRT %s, %s are not relatively prime GCD = %s" % (m_list[j], m_list[i], z))
                # end program
                sys.exit()
        else:
            continue
    if j == len(m_list) - 2:
        M *= m_list[-1]
        text_to_print += ('· m%s' % (j + 2))
        print("\nM = %s = %s \n" % (text_to_print, M))
f = 1
# calculate N1,...,Nt and H1,...,Ht
for r in m_list:
    n_list.append(M // r)
    print("N%s = M/m%s = %s/%s = %s\t" % (f, f, M, r, M // r))
    print("N%s = %s = %s mod %s \t" % (f, M // r, ((M // r) % r), r))
    h = inverse((M // r) % r, r)
    print("H%s = inverse(%s) mod %s = %s\n" % (f, ((M // r) % r), r, h))
    h_list.append(h)
    f += 1
print("\nx = a1·N1·H1 + ... +at·Nt·Ht")
x = 0
print("x = ", end='')
# x = a1 M1 y1+...+at Mt yt, where t is number of eqns
for (e, v, c) in zip(a_list, n_list, h_list):
    print("%s·%s·%s" % (e, v, c), end='')
    print(" + ", end="") if v != n_list[-1] else print(" (mod %s)" % M)
    x += e * v * c
print("  = %s mod %s" % (x, M))
print("  = %s mod %s" % (x % M, M))
