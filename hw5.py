'''
1a. [3,5,4,0,1,2] o [4,5,3,1,2,0] = 
    [3,5,4,0,1,2] o [4,5,3,1,2,0] = [1,x,x,x,x,x]
    [3,5,4,0,1,2] o [4,5,3,1,2,0] = [1,0,x,x,x,x]
    [3,5,4,0,1,2] o [4,5,3,1,2,0] = [1,0,2,x,x,x]
    [3,5,4,0,1,2] o [4,5,3,1,2,0] = [1,0,2,4,x,x]
    [3,5,4,0,1,2] o [4,5,3,1,2,0] = [1,0,2,4,5,x]
    [3,5,4,0,1,2] o [4,5,3,1,2,0] = [1,0,2,4,5,3]

1b. [441,...,999,0,...,440] o [176,...,999,0,...175]
    441 + 176 mod 1000 = 617 mod 1000
    = [617,...,999,0,...616]

1c. p o p o [4,5,6,0,1,2,3] = for p as a swap permutation in S7	
    p = [0,1,4,3,2,5,6]
    p o p = [0,1,4,3,2,5,6] o [0,1,4,3,2,5,6] =
    [0,1,4,3,2,5,6] o [0,1,4,3,2,5,6] = [0,x,x,x,x,x,x]
    [0,1,4,3,2,5,6] o [0,1,4,3,2,5,6] = [0,1,x,x,x,x,x]
    [0,1,4,3,2,5,6] o [0,1,4,3,2,5,6] = [0,1,2,x,x,x,x]
    ...
    [0,1,4,3,2,5,6] o [0,1,4,3,2,5,6] = [0,1,2,3,4,5,6]
    [0,1,2,3,4,5,6] o [4,5,6,0,1,2,3] =
    [4,5,6,0,1,2,3]

1d. q^-1 o p^-1 o q^-1 o q o p o q    = where q and p are cyclic permutations in C5
    p = [1,2,3,4,0], q = [3,4,0,1,2]
    p^-1 = [2,3,4,0,1] q^-1 = [1,2,3,4,0]
    [1,2,3,4,0] o [2,3,4,0,1] o [1,2,3,4,0] o [3,4,0,1,2] o [1,2,3,4,0] o [3,4,0,1,2] =
    [3,4,0,1,2] o [1,2,3,4,0] o [3,4,0,1,2] o [1,2,3,4,0] o [3,4,0,1,2] =
    [4,0,1,2,3] o [3,4,0,1,2] o [1,2,3,4,0] o [3,4,0,1,2] =
    [2,3,4,0,1] o [1,2,3,4,0] o [3,4,0,1,2] =
    [3,4,0,1,2] o [3,4,0,1,2] =
    [1,2,3,4,0] which is the same as q^-1   

1e. (C2, o) = [0,1],[1,0]
    -> [0,1] o [0,1] = [0,1] -> map this as a
    -> [0,1] o [1,0] = [1,0] -> map this as b
    -> [1,0] o [0,1] = [1,0] -> already exists as b
    -> [1,0] o [1,0] = [0,1] -> already exists as a
    final map = [a,b,b,a]
    
    ((ℤ/4ℤ)*, ⋅) = 1,3
    -> 1 * 1 mod 4 = 1 -> map this as a
    -> 1 * 3 mod 4 = 3 -> map this as b
    -> 3 * 1 mod 4 = 3 -> already exists as b
    -> 3 * 3 mod 4 = 1 -> already exists as a
    final map = [a,b,b,a]
    [a,b,b,a] = [a,b,b,a] means this is isomorphic

1f. (closure({3 + 80ℤ}, ⋅), ⋅) & (ℤ/4ℤ, +)
    (ℤ/4ℤ, +) = 1,3 = [2,1,1,2] or [a,b,b,a]
    {3, 3*3, 3*3*3, 3*3*3*3, 3*3*3*3*3, 3^6...} = {3,9,27,1,3,9...} -> {3,9,27,1}
    There is no bijection because the sets to be compared are not the same length.
    One set is {1,3} and the other {3,9,27,1}

1g. There is no isomorphism here because the two algebraic structures are not the same
    in size, the first has a length of 4 while the second has a length of 2 because 4
    only has two coprimes: 1 and 3.

'''
from math import floor
from fractions import gcd
from random import randint
from urllib.request import urlopen

#2a
def permute(p, l):
    #permutation p list of ints and list l of same length: returns permutation of l
    return[ l[ p[ x ] ] for x in range( len ( p ) ) ]

#2b
def C(k, m):
    #ints k, m: returns cyclic permutation of Cm shift by k
    return[ ( ( x + k ) % m ) for x in range( m ) ]

#2c
def M(a, m):
    #coprime ints a, m: 0 < a < m: returns multiplication permutation of Mm; a % m
    return[ ( ( x * a ) % m ) for x in range( m ) ]

#2d
def sortHelper(l):
    #checks if sorted
    a = len( l )
    for x in range( a ):
        if x != 0 :
            if l[ x ] < l[ x-1 ]: return False
    return True

def sort(l):
    #list l of ints: returns list to permute into ascending order
    
    a = len( l )
    p = [ x for x in range( a ) ]
    
    for x in range( 1, a ):
        p = C( x,a )
        q = permute( p, l )

        if sortHelper( q ):
            return p

        p = M( x, a )
        k = permute( p,l )

        if sortHelper( k ):
            return p
        
    return None

#from notes
def unreliableUntrustedProduct(xs, n):
    url = 'http://cs-people.bu.edu/lapets/235/unreliable.php'
    return int(urlopen(url+"?n="+str(n)+"&data="+",".join([str(x) for x in xs])).read().decode())

'''taken from previous homeworks'''
def egcd(a, b):
    (x, s, y, t) = (0, 1, 1, 0)
    while b != 0:
        k = a // b
        (a, b) = (b, a % b)
        (x, s, y, t) = (s - k*x, x, t - k*y, y)
    return (s, t)
def findCoprime(m):
    for b in range(m // 2, m - 1):
        if m % 2 == 1: #is odd
            return pow(2, b)
        if gcd(b, m) == 1 & (m != b):
            return b
    return m + 1
def inv(a, m):
    (s, t) = egcd(a, m)
    if (a*s) + (m*t) == 1: #are coprimes
        return s % m
    return None
def encrypt(m,t):
    #int m and tuple t: ( n,e ) public key and returns ciphertext c
    ( n,e ) = t
    return pow( m,e,n )
def decrypt(c,t):
    #int c -> ciphertext and tuple t: ( n,d ) RSA private key
    ( n,d ) = t
    return pow( c,d,n )
''''''

#3a
def privateProduct(xs, p, q):
    #q prime to create public and private for RSA, encrypt all ints in xs mod n
    crypt = []
    
    #code taken from generate function in hw4
    z = ( p-1 )*( q-1 )
    n = p*q
    for e in range( 2,z-1 ):
        if gcd( e,z ) == 1: break
    d = inv( e,z )
    #
    
    for x in xs:
        crypt.append( encrypt( x,( n,e ) ) )
        
    prod = unreliableUntrustedProduct( crypt,n )
    dProd = decrypt( prod, ( n,d ) )
    
    return dProd % p

'''from previous homeworks'''
def solveOne(c, b, a, m):
    a -= b #get rid of b
    b = 0
    
    (x, y) = egcd(c, m) 
    if (c*x) + (m*y) == 1: #are coprimes or gcd(c,m) == 1:
        
        return (a*inv(c,m)) % m
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
        x1 = a * n * inv(n,m)
        x2 = r * m * inv(m,n)

        return (x1+x2) % (m*n)
    return None
''''''

#3b
def validPrivateProduct(xs, p, q):
    #makes sure to return a correct solution using the unreliableUntrustedProduct
    crypt = []
    r = randint( 2,q )
    n = p*q
    
    for i in xs:
        crt = ( i*q*inv( q,p ) ) + ( r*p*inv( p,q ) )
        crypt.append( crt % n ) #solve for Z/nZ

    prod = privateProduct( crypt,p,q )

    #check if correct
    if pow( r,len( xs ),q ) == prod % q: return prod
    return validPrivateProduct( crypt,p,q ) #keep going until we get a correct solution

#4
def isomorphism(A,B):
    #tuples: (ordered list from alg structure, function on said elements)->(A, ⊕)&(B, ⊗)
    ( a,opA ) = A
    ( b,opB ) = B
    aSet = []
    bSet = []
    
    if len( a ) != len( b ): return None #if they do not have the same length, no isomorph
    
    for x in range( len( a ) ): #for each number in A and B, len should be the same
        for y in range( len( a ) ):
            aSet.append( opA( a[x],a[y] ) )
            bSet.append( opB( b[x],b[y] ) )
            
    #print( "", aSet, "\n", bSet )
    m = isoHelper( aSet )
    n = isoHelper( bSet )
    #print( "", m, "\n", n )
    return m == n
    #return isoHelper( m,n )

def isoHelper(a):
    #returns one list mapping values
    aSet = [0] * len( a )
    for x in range( len( a ) ): #go through all values and add their index to aSet
        aLess = a[ 0:x ] #set of all but the current value
        
        if x+1 < len( a ):
            aMore = aLess
            aMore.append( a[ x+1: ] ) #add values after current value
            
            if a[ x ] in aMore: #already exists
                aSet[ x ] = aMore.index( a[ x ] ) #set value to index of first instance
            else: aSet[ x ] = x #first instance, set to current index
            
        else:
            if a[ x ] in aLess: #already exists
                aSet[ x ] = aLess.index( a[ x ] ) #set value to index of first instance
            else: aSet[ x ] = x #first instance, set to current index
            
    return aSet
