def is_prime(n):
    # basic rules, 1 is not prime but 2 is the first prime.
    if n == 1:
        return False
    elif n == 2:
        return True
    # checking if there a prime j divides n, where 1 < j <= sqrt(n)
    # why sqrt(n) not n ?
    # first from fundamental theory of arithmetic
    # every integer can be written as a product of primes
    # if a number have a prime divisor p, then 1 < p <= sqrt(n)
    # so if n is composite we will find it's prime factor <= sqrt(n)
    # otherwise if no prime factor appears then n is prime
    m = int((n ** 0.5) + 1)
    for j in primes:
        # if j divides n then n is not prime
        if n % j == 0:
            return False
        # if j exceeds sqrt(n) so no prime divisors then n is prime
        elif j >= m:
            return True


# creating our list of primes, initially empty
primes = []
# define two counters for primes of the form 4k+1 and 4k+3
k_1, k_3 = 0, 0
# just formatting columns names
print('\n', '{:>12}'.format(""), '{0:^20}'.format("# of primes < x"), end="")
print('{0:^35}'.format("# of primes of the form 4k+1 "), end="")
print('{0:^33}'.format("# of primes of the form 4k+3 "))
# loop through numbers from 1 to 10000
for i in range(1, 10001):
    # if i is prime add i to our list of primes
    if is_prime(i):
        primes.append(i)
        # see if this prime is on form 4k+1 or 4k+3
        if i % 4 == 1:
            k_1 += 1
        elif i % 4 == 3:
            k_3 += 1
    # printing results at 1000,2000,...,10000
    if i % 1000 == 0:
        print('{0:^13}'.format("x = %s" % i), end='')
        print('{0:^22}'.format(len(primes)), end='')
        print('{0:^31}'.format(k_1), end='')
        print('{0:^37}'.format(k_3))
