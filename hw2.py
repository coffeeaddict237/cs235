'''
1)
a. 4x + 1 ≡ 9 (mod 17)
    4x ≡ 8 (mod 17)
    x ≡ 2 (mod 17)

b. 5x + 2 ≡ -6 (mod 11)
    5x ≡ -8 (mod 11)
    -8 + 11z = {-8,3,14,25..}
    5x ≡ 25
    x ≡ 5 (mod 11)

c. 10x - 2 ≡ 3 (mod 5)
    10x ≡ 5 (mod 5)
    5 + 5z ≡ {5,10...}
    10x ≡ 10
    x ≡ 1 (mod 5)

d. 17x + 44 ≡ 333 (mod 389)
    17x ≡ 289 (mod 389)
    x ≡ 17 (mod 389)

e. 16x + 1 ≡ 3 (mod 8)
    16x ≡ 2 (mod 8)
    2 + 8z ≡ {2,10,18,26,34,40,48...}
    16x ≡ 48
    x ≡ 3 (mod 8)

f. 5x + 7 ≡ 13 (mod 29)
    5x ≡ 6 (mod 29)
    6 + 29z ≡ {6,35...}
    5x ≡ 35
    x ≡ 7 (mod 29)

g. 11x + 5x ≡ 64 (mod 587)
    16x ≡ 64 (mod 587)
    64 + 587x ≡ {64}
    x ≡ 1 (mod 587)

h. 146467848x ≡ 43698243047256 (mod 7777777777777777777777777)
    x ≡ 298347 (mod 7777777777777777777777777)
    
i. 650472472230302x ≡ 1 (mod 8910581811374)
    {1,8910581811375,17821163622749,26731745434123,35642327245497,44552909056871,53463490868245,62374072679619}
    
'''
import math
from fractions import gcd
from math import log

#from lecture notes -> greatest common divisor
#def gcd(x, y):
 #return max({z for z in range(0, min(x,y)) if x % z == 0 and y % z == 0})

#2a

def closest(t,ks):
    mini = 0
    for i in range(len(ks)):
        if (abs(mini-t)) > (abs(ks[i]-t)):
            mini = ks[i]
    return mini

#2b

def findCoprime(m):
    for b in range(m // 2, m - 1):
        if m % 2 == 1: #is odd
            return 2 ** b
        if gcd(b, m) == 1 & (m != b):
            return b
    return m + 1

#2c

def randByIndex(m, i):
    #i is the index
    a = findCoprime(m) #a & m are coprime
    s = closest((4/7 * m), [a**k for k in range(1, m.bit_length())])
    return (a * i) % m

#3

def probablePrime(m):
    #m >= 1
    for x in range(100):
        a = randByIndex(m - 1, 2)
        if m % a == 0: #if anything divides m evenly from randomly gen number
            return False
        if gcd(a, m) != 1: #not coprimes
            return False
        if(pow(a, (m - 1), m) != 1):
            return False
    return True

#4

def makePrime(d):
    n = randByIndex(((10 ** d) - 1), (2 ** (d // 2) + 1))
    while probablePrime(n) == False:
        n = randByIndex(((10 ** d) - 1), (10 ** (d // 2) + 1))
        return n
