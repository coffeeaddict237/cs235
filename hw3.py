'''
1a) 5x = 3 (mod 11) -> x = 5 (mod 11)
3 + 11x = [3, 14, 25]
25 / 5 = 5
5^-1 mod 11 = 9

1b) 8x - 1 = 1 (mod 5) -> 8x = 2 (mod 5)
2 + 5x = [2,7,12,17,22,27,32]
32 / 8 = 4
4^-1 mod 5 = 4

1c) 
x = 4 (mod 7)
4^-1 mod 7 = 2

x = 3 (mod 5)
3^-1 mod 5 = 2

1d) x = 3 (mod 5)
3^-1 mod 5 = 2

x = 6 (mod 14) does not have an inverse because 6 and 14 are not coprimes

1e) x = 10 (mod 11)
10^-1 mod 11 = 10

3x = 1 (mod 4)
1 + 4x = [1,5,9]
9 / 3 = 3
3^-1 mod 4 = 3

1f) qx = 3 (mod p)
x1 = 2 (mod q)
x1 = (3* q^-1) (mod p)
x1 = (3* q^-1 mod p) * q * (q^-1 mod p)
x2 = 2 * p * (p^-1 mod q)
= x1 + x2 mod p*q
= (3* q^-1 mod p) * q * (q^-1 mod p) + 2 * p * (p^-1 mod q)

'''
from math import floor
from fractions import gcd
from random import randint

#2a
def invPrime(a, p):
    if a == 0:
        return None
    return pow(a, p-2, p)

#from notes
def egcd(a, b):
    (x, s, y, t) = (0, 1, 1, 0)
    while b != 0:
        k = a // b
        (a, b) = (b, a % b)
        (x, s, y, t) = (s - k*x, x, t - k*y, y)
    return (s, t)

#2b
def inv(a, m):
    (s, t) = egcd(a, m)
    if (a*s) + (m*t) == 1: #are coprimes
        return s % m
    return None

#3a

def solveOne(c, b, a, m):
    #print(c, "* x +", b, "=", a, "( mod",m, ")")
    a -= b #get rid of b
    b = 0
    #print("Solve one:", c, "* x =", a, "( mod",m, ") = ")
    
    (x, y) = egcd(c, m) 
    if (c*x) + (m*y) == 1: #are coprimes or gcd(c,m) == 1:
        
        #print((a*inv(c,m)) % m)
        return (a*inv(c,m)) % m
    return None

#3b

def solveTwo(e1, e2):
    (c,b,a,m) = e1
    (t,s,r,n) = e2
    (x,y) = egcd(m, n)
    if solveOne(c,b,a,m) != None and solveOne(t,s,r,n) != None and (m*x) + (n*y) == 1:
        #subtract to get rid of b&s if not 0
        a -= b
        r -= s
        #multiply by inverse to get rid of c&t if not 1
        if c != 1:
            a = a*inv(c,m)
        if t != 1:
            r = r*inv(t,n)

        #now the format is: x = a mod m / x = r mod n
            
        #x1 ≡ a ⋅ n ⋅ n-1 (mod (m ⋅ n))
        x1 = a * n * inv(n,m)
        #x2 ≡ r ⋅ m ⋅ m-1 (mod (m ⋅ n))
        x2 = r * m * inv(m,n)
        print("Inverse n,m:", inv(n,m), "Inverse m,n:", inv(m,n))
        print("x1:(", x1, ") & x2:(", x2, ") =", (x1+x2), "...mod", (m*n), "=", (x1+x2) % (m*n))
        return (x1+x2) % (m*n)
    return None

#3c

def solveAll(es):
    while(es):
        e1 = es.pop(0)
        (c,b,a,m) = e1 
        #print(c, "* x +", b, "=", a, "( mod",m, ")")
        
        if len(es) == 0:
            return a #no more equations return the answer
        
        e2 = es.pop(0)
        (t,s,r,n) = e2
        #print(t, "* x +", s, "=", r, "( mod",n, ")")
        
        ans = solveTwo(e1,e2)
        if ans== None: #if at any point two equations cannot be solved return None
            return None
       
        #print("One set down:")              
        e3 = (1,0,ans,m*n)
        #print(1, "* x =", ans, "( mod",m*n, ")")
        
        es.insert(0, e3) #insert answer back into the list
    return None

#4a

def sumPowsModPrime(nes, p):
    return sum([pow(x[0],x[1],p) for x in nes]) % p

#4b

def sumPowsModPrimes(nes, ps):
    return solveAll([(1,0,sumPowsModPrime(nes,p),p) for p in ps])
