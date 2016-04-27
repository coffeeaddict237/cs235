'''
1.a.k = 20 bits long length(p*q) = k
    compute x = (...((c^e1)^e2)^e3...)^eu) (mod p*q)
    [x^y mod m] takes k^3 time steps -> 20^3 -> 8000
    c^e1 mod p*q takes k^3 time * u operations = k^3 * u time steps
    20^3 * u -> 8000u time steps

  b.now k = 10 bits long
    a = c^e1...(mod p) & b = c^e1..(mod q)
    will both take 10^3 * u steps each -> 2000 * u
    
    x = a mod p
    x = b mod q
    Finding the solution to the above system of equations: 16 * k^3 steps
    16 * 10^3 = 16000
    
  c.8000u > 2000u + 16000
    6000u > 16000
    u > 3

2.a.x^2 = 25 mod 43
    x = ±5 mod 43
    {5,38}

  b.x^2 = 5 mod 19
    19 % 4 = 3 --> 5^(19+1/4) mod 19
    5^5 mod 19 -> (5^2 mod p)^2 * 5 mod 19 -> 6^2 mod 19 * 5 -> 36 mod 19 * 5
    17 * 5 mod 19 = 85 % 19
    x = ±9 mod 19
    {9,10}

  c.x^2 = 1 mod 55{ x^2 = 1 mod 5 , x^2 = 1 mod 11 }
    x^2 = 1 mod 5 -> x = ±1 mod 5 -> {1,4}
    x^1 = 1 mod 11 -> x = ±1 mod 11 -> {1,10}

    x = 1 mod 5
    x = 1 mod 11
    CRT -> [1*11^-1*11] + [1*5^-1*5] -> [1*11] + [9*5]
    56 mod 55 -> 1 mod 55
    
    x = 1 mod 5
    x = 10 mod 11
    CRT -> [1*11^-1*11] + [10*5^-1*5] -> [1*11] + [10*9*5]
    11 + 450 -> 461 mod 55 -> 21 mod 55

    x = 4 mod 5
    x = 1 mod 11
    CRT -> [4*11^-1*11] + [1*5^-1*5] -> [4*11] + [9*5]
    44 + 45 -> 89 mod 55 -> 34 mod 55
    
    x = 4 mod 5
    x = 10 mod 11
    CRT -> [4*11^-1*11] + [10*5^-1*5] -> [4*11] + [10*45]
    44 + 450 -> 494 mod 55 -> 54 mod 55

    {1,21,34,54}
    
  d.3x^2 = 7 mod 41 * 3^-1
    3^-1 = 14 mod 41 -> 7 * 14 -> 98 mod 41 = 16
    x^2 = 16 mod 41 -> x = ±4 mod 41
    {4,37}
    
  e.x^2 = 8 mod 49 -> x^2 = 8 mod 7, k = 1
    7 % 4 = 3 -> 8^(7+1/4)-> 64 mod 7 -> ±1 mod 7
    1^-1 * 2^-1 * ((r-x^2)/p^k)(mod p)
    1^6 * 2^6 * ((8 - 1)/7)) mod 7 -> Ф6 = (2-1)*(3-1) = 2
    1 * 2^2 * (7/7) mod 7 -> 4 * 1 mod 7 -> 4 mod 7
    y = 4 + 4 * 7 mod 49
    y = 4 + 28 mod 49 -> ±32 mod 49
    {17,32}

  f.(8*x^2) + 4 = 6 mod 21
    8x^2 = 2 mod 21 * 8^-1 -> 8
    x^2 = 16 mod 21 -> {x^2 = 16 mod 7 , x^2 = 16 mod 3}
    x^2 = 2 mod 7 , x^2 = 1 mod 3
    x = ±1 mod 3 -> {1,2}
    7%4 = 3 --> 2^(7+1/4) -> 2^2 -> 4
    x = ±4 mod 7 -> {4,3}

    x = 1 mod 3
    x = 4 mod 7
    CRT -> [1*7^-1*7] + [4*3^-1*3] -> [1*7] + [4*5*3]
    7 + 60 -> 67 mod 21 -> 4 mod 21
    
    x = 1 mod 3
    x = 3 mod 7
    CRT -> [1*7^-1*7] + [3*3^-1*3] -> [1*7] + [3*5*3]
    7 + 45 -> 52 mod 21 -> 10 mod 21
    
    x = 2 mod 3
    x = 4 mod 7
    CRT -> [2*7^-1*7] + [4*3^-1*3] -> [2*1*7] + [4*5*3]
    14 + 60 -> 74 mod 21 -> 11 mod 21
    
    x = 2 mod 3
    x = 3 mod 7
    CRT -> [2*7^-1*7] + [3*3^-1*3] -> [2*7] + [3*5*3]
    14 + 45 -> 59 mod 21 -> 17 mod 21

    {4,10,11,17}

'''

'''Helpers for question 3 taken from homework 3'''
from math import floor
from fractions import gcd
from random import random

def egcd(a, b):
    (x, s, y, t) = (0, 1, 1, 0)
    while b != 0:
        k = a // b
        (a, b) = (b, a % b)
        (x, s, y, t) = (s - k*x, x, t - k*y, y)
    return (s, t)
def inv(a, m):
    (s, t) = egcd(a, m)
    if (a*s) + (m*t) == 1: #are coprimes
        return s % m
    return None
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
        #print("Inverse n,m:", inv(n,m), "Inverse m,n:", inv(m,n))
        #print("x1:(", x1, ") & x2:(", x2, ") =", (x1+x2), "...mod", (m*n), "=", (x1+x2) % (m*n))
        return (x1+x2) % (m*n)
    return None
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
        #sqrts(1, [(7,1), (11,1), (3,1)])print(1, "* x =", ans, "( mod",m*n, ")")
        
        es.insert(0, e3) #insert answer back into the list
    return None
''''''

#3a 
def sqrtsPrime(a,p):
    if p % 4 == 3:
        
        b = ( p+1 ) // 4
        s = pow( a,b,p )
        c = p - s
        
        if pow( s,2,p ) == a and pow( c,2,p ) == a:
            return ( s,c )
    return None

#3b 
def sqrtsPrimePower(a,p,k):
    if sqrtsPrime( a,p ) == None: return None
    
    if k == 1:
        return sqrtsPrime( a,p )
    
    d = pow( p,k )
    s = pow( p,k-1 )
    
    ( x,y ) = sqrtsPrimePower( a,p,k-1 )
    
    #x^-1 * 2^-1 * ((a - x^2) // s ) mod p
    c = inv( x,p ) * inv( 2,p ) * ( ( a - pow( x,2 ) ) // s )
    c = c % p

    #x + c * s mod d
    ans = x + c*s
    ans = ans % d

    z = d - ans
    return ( ans,z )
	    
#from notes
def combinations(ls):
    if len(ls) == 0:
        return [[]]
    else:
        return [ [x]+l for x in ls[0] for l in combinations(ls[1:]) ]

#3c
def sqrts(a, pks):
    ans = []
    i = 1
    for ( p,k ) in pks:
        d = pow( p,k )
        ( x,y ) = sqrtsPrimePower( a,p,k )

        #for the base case, first equation to be inserted
        if i == 1:
            ans.append( x )
            ans.append( y )
            i *= d

        #continue adding equations while simultaneously solving them           
        else:
            z = [ ]
            for e in ans:
                z.append( solveTwo( ( 1,0,x,d ), ( 1,0,e,i ) ) )
                z.append( solveTwo( ( 1,0,y,d ), ( 1,0,e,i ) ) )
            ans = z
            i *= d
            
    return ans

#4a
def factorsFromPhi(n,phi_n):
    #n is a product of two distinct prime numbers and phi_n = φ(n)
    x = phi_n - n - 1
    #x = ( -b +- sqrt(b^2 - 4ac) ) // 2a ---> b = x , c = n
    y = pow( ( ( pow(x,2) - (4 * n) ) ) , 0.5 )
    z = int( ( (-x) - y ) // 2 )
    y = int( ( (-x) + y ) // 2 )
    return ( y,z )

#4b
def factorsFromRoots(n,x,y):
    #n is a product of two distinct prime numbers and x^2 = y^2 mod n
    p = gcd( n,x+y )
    q = gcd( n,x-y )
    if p < 0 and q < 0: return ( -p,-q )
    elif q < 0: return ( p,-q )
    elif p < 0: return ( -p,q )
    return ( p,q )


'''Helpers for question 5 taken from homework 2'''
def closest(t,ks):
    mini = 0
    for i in range(len(ks)):
        if (abs(mini-t)) > (abs(ks[i]-t)):
            mini = ks[i]
    return mini

def findCoprime(m):
    for b in range(m // 2, m - 1):
        if m % 2 == 1: #is odd
            return pow(2, b)
        if gcd(b, m) == 1 & (m != b):
            return b
    return m + 1

def randByIndex(m, i):
    #i is the index
    a = findCoprime(m) #a & m are coprime
    s = closest((4/7 * m), [pow(a,k) for k in range(1, m.bit_length())])
    return (a * i) % m

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

def randInRange(minR, maxR):
    diff = maxR - minR
    return floor(random() * diff + minR)

def makePrime(d):
    maxR = pow(10, d) - 1
    minR = pow(10, d - 1)

    # n must be in {10**(d - 1), ..., 10**d - 1}
    n = randInRange(minR, maxR)

    while not probablePrime(n):
        n = randInRange(minR, maxR)
    return n
''''''

#5a
def generate(k):
    #return tuple of ( n,e,d ), n & e are public
    x = makePrime( k )
    y = makePrime( k )
    z = ( x-1 )*( y-1 )
    
    n = x*y
    for e in range( 2,z-1 ):
        if gcd( e,z ) == 1: break
    d = inv( e,z ) % z
    return( n,e,d )

#5b
def encrypt(m,t):
    #int m and tuple t: ( n,e ) public key and returns ciphertext c
    ( n,e ) = t
    return pow( m,e,n )

#5c
def decrypt(c,t):
    #int c -> ciphertext and tuple t: ( n,d ) RSA private key
    ( n,d ) = t
    return pow( c,d,n )
   
