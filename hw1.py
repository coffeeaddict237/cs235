import math
'''1'''

#a
def perfectSquares(n):
    #takes int n and returns all perfect squares up to n
    N = int(math.sqrt(n)) + 1
    return {x * x for x in range(1, N)}

#b
def squareFree(n):
    #takes int n and returns if n is free of any square factors
    squares = {x for x in range(2, (n + 1)) if math.sqrt(x) % 1 == 0}
    S = {x for x in squares if n % x == 0} #checks if any are factors
    return len(S) == 0; #if len is 1, then there is a square factor, return false

#c
def same(n, m):
    #returns true if both are squares or if they are both not squares
    return ( (math.sqrt(n) % 1 == 0) & (math.sqrt(m) % 1 == 0) or \
             (not(math.sqrt(n) % 1 == 0)) &  (not(math.sqrt(m) % 1 == 0)) )

#d
def separate(S):
    #create subsets with squares and non squares grouped together
    return {(x,y) for x in S for y in S if same(x,y)}

#e
notReflexiveOn = 0 #no counterexample exists
notSymmetricOn = 0 #no counterexample exists
notTransitiveOn = 0 #no counterexample exists

'''2'''
#from notes
def relation(R, X):
  return R.issubset(product(X, X))

#from notes
def forall(X, P):
  S = {x for x in X if P(x)}
  return len(S) == len(X)

#a
def isReflexive(X,R):
    #set X relation R, return true if reflexive relation of X using forall
    return forall(X, lambda x:((x,x) in R))

#b
def isSymmetric(X,R):
    #set X relation R, return true if symmetric relation of X using forall
    return forall(X, lambda x: forall(X, lambda y:((x,y) in R) <= ((y,x) in R)))

#c
def isTransitive(X,R):
    #set X relation R, return true if transitive relation of X using forall
    return forall(X, lambda x: forall(X, lambda y: forall(X, lambda z: ((x,y) in R \
    and (y,z) in R) <= ((x,z) in R))))

#d
def isEquivalence(X,R):
    #must have reflexive symmetric and transitive relations
    return isReflexive(X,R) and isSymmetric(X,R) and isTransitive(X,R)

'''3'''

def quotient(X, R): #from assignment sheet
    return {frozenset({y for y in X if (x,y) in R}) for x in X}
#a
X1 = {"a","b","c","d","e","f"}
R1 = {("a","a"),("b","b"),("c","c"),("d","d"),("e","e"),("f","f"),("a","c"),("c","a")\
      ,("b","d"),("d","b"),("e","f"),("f","e")}

#b
X2 = {0,1,2,3,4,5,6,7,8,9,10,11}
R2 = {(0,0),(1,1),(2,2),(3,3),(4,4),(5,5),(6,6),(7,7),(8,8),(9,9),(10,10),(11,11),\
      (0,0),(0,2),(2,0),(2,4),(4,2),(2,6),(6,2),(8,2),(2,8),(2,10),(10,2),\
      (0,4),(4,0),(4,6),(6,4),(4,8),(8,4),(10,4),(4,10),\
      (0,6),(6,0),(6,8),(8,6),(6,10),(10,6),\
      (8,0),(0,8),(8,10),(10,8),(10,0),(0,10),\
      (1,3),(3,1),(3,5),(5,3),(3,7),(7,3),(3,9),(9,3),(3,11),(11,3),\
      (1,5),(5,1),(5,7),(7,5),(5,9),(9,5),(5,11),(11,5),\
      (1,7),(7,1),(7,9),(9,7),(7,11),(11,7),\
      (1,9),(9,1),(9,11),(11,9),(11,1),(1,11)}

#c
def rangeForSet(n,m):
    #returns true when both numbers are in range(0,30) or (30,60) or (60,90)
    return (n in range(0,30) and m in range(0,30)) or \
           (n in range(30,60) and m in range(30,60)) or \
           (n in range(60,90) and m in range(60,90))

def rangeSet(S):
    #returns a equivalence set for set X3
    return {(x,y) for x in S for y in S if rangeForSet(x,y)}

X3 = set(range(0,90))
R3 = rangeSet(X3)

'''4'''
C1 = {'Iceland', 'Vietnam', 'Kazakhstan', 'Australia'}
D1 = {('Vietnam', 'Kazakhstan'), ('Kazakhstan', 'Vietnam'),\
     ('Iceland','Iceland'), ('Australia','Australia'),\
     ('Vietnam','Vietnam'),('Kazakhstan','Kazakhstan')}

C2 = {'Iceland', 'Vietnam', 'Kazakhstan', 'Australia', 'Ukraine', 'Poland', 'Germany'}
D2 = {('Vietnam', 'Vietnam'), ('Kazakhstan','Kazakhstan'),\
     ('Poland','Poland'), ('Ukraine','Ukraine'), ('Germany','Germany'),\
     ('Australia','Australia'),('Iceland','Iceland'),\
     ('Vietnam', 'Kazakhstan'), ('Kazakhstan', 'Vietnam'), \
     ('Ukraine', 'Poland'), ('Poland', 'Ukraine'), \
     ('Germany', 'Poland'), ('Poland', 'Germany'),\
     ('Ukraine','Germany'), ('Germany','Ukraine')}

C3 = {'Iceland', 'Vietnam', 'Kazakhstan', 'Australia', 'Ukraine', 'Poland', 'Germany'}
D3 = {('Vietnam', 'Vietnam'), ('Kazakhstan','Kazakhstan'),\
     ('Poland','Poland'), ('Ukraine','Ukraine'), ('Germany','Germany'),\
     ('Australia','Australia'),('Iceland','Iceland'),\
     ('Vietnam', 'Kazakhstan'), ('Kazakhstan', 'Vietnam')}

#a
def minimumFlights(C,D):
    #returns the minimum flights necessary to reach all countries in set C
    #my set D includes reflexive relations as well in order to pass through quotient
    return len(quotient(C,D)) - 1

#b
def longestDrive(C,D):
    #returns the number of countries you can visit in one continuous drive
    return max({len(x) for x in quotient(C,D)}) #find quotient and return the length of the longest

#tests:
#print('Minimum from sheet:', minimumFlights(C1,D1))
#print('Longest from sheet:',longestDrive(C1,D1))
#print('Minimum separate a:',minimumFlights(C2,D2))
#print('Longest separate a:',longestDrive(C2,D2))
#print('Minimum separate b:',minimumFlights(C3,D3))
#print('Longest separate b:',longestDrive(C3,D3))

