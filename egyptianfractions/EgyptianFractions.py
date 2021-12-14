## This algorithm calculates the egpytian fraction of a number lower than 1
import math

def egpytian_fraction(num,den):
    denom = []
    while num != 0:
        new_den = math.ceil(den/num)
        denom.append(new_den)
        num = new_den * num - den
        den = den * new_den
    print(denom)
