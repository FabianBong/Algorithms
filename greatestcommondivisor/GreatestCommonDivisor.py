## This algorithm finds the gcd of two numbers

def brute_force(u, v):
    t = min(u, v)

    for i in range(t, 1, -1):
        if u % i == 0 and v % i == 0:
            return i

    return 1


## This is a terrible way, it requires O(min(u,v))


## Another algorithm relies on math

def euclid(u, v):
    while v != 0:
        u, v = v, u % v
    return u


## We can do even better and avoid division (to increase speed)

def binary_gcd(u, v):
    if u < v:
        return binary_gcd(v, u)
    if v == 0:
        return u
    if u % 2 == 0 and v % 2 == 0:
        return 2 * binary_gcd(u / 2, v / 2)
    if u % 2 != 0 and v % 2 == 0:
        return binary_gcd(u, v / 2)
    if u % 2 == 0 and v % 2 != 0:
        return binary_gcd(u / 2, v)
    return binary_gcd((u - v) / 2, v)


## With analysis we can prove that O(max(lg u, lg v))