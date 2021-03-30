from main import *
import random


def primeGen(k):
    p = random.getrandbits(k)
    a = random.randint(2, p - 1)
    while fermat(a, p) == 'tak' and p % 4 != 3:
        p = random.getrandbits(k)
        a = random.randint(2, p - 1)
    return p

def genAB(p):
    A = random.randint(0, p - 1)
    B = random.randint(0, p - 1)
    return A, B

#Zadanie1
def RandABp(k):
    p = primeGen(k)
    (A, B) = genAB(p)
    while dodaj(mnoz(poteg(A,3,p),4), mnoz(poteg(B,2,p),27)) % p == 0:
        (A, B) = genAB(p)
    return A, B, p


#Zadanie2
def RandABpxy(a, b, p):
    p = p
    A = a
    B = b
    (x, y) = genAB(p)
    while not ((poteg(y,2,p)) % p == (dodaj(dodaj(poteg(x,3,p),mnoz(A,3)),B)) % p):
        (x, y) = genAB(p)
    return(A,B,p,x,y)

#Zadanie3
def RandABpxyYN(a, b, p, x, y):
    if (poteg(y,2,p) % p) == (dodaj(dodaj(poteg(x,3,p),mnoz(a,3)),b) % p):
        return(a, b, p, x, y, "TRUE")
    else:
        return(a, b, p, x, y, "FALSE")



#Zadanie4
def Randpxyx1y1(p, x, y):
    (x1, y1) = genAB(p)
    while (x != x1 % p) or (y != (y1 * -1) % p):
        (x1, y1) = genAB(p)
    return(p, x, y, x1,y1)



#Zadanie5
def SumPtABpx1y1x2y2x3y3(a, b, p, x1, y1, x2, y2):
    z = 0
    B = b
    P = [x1, y1]
    Q = [x2, y2]
    if (P == z):
        return Q
    if (Q == z):
        return P
    if P[0] == Q[0]:

        if P[0] == Q[0] and P[1] == (-1 * Q[1]) % p:
            return (a, b, p, x1, y1, x2, y2,float('inf'), float('inf'))
        else:
            m = mnoz((dodaj(mnoz(3, poteg(P[0], 2, p)),a)), poteg(mnoz(2, P[1]), check(p,2), p)) % p
    else:
        m = mnoz((check(P[1],Q[1])),poteg(check(P[0],Q[0]), check(p,2), p)) % p
    x = check(check(poteg(m, 2, p), P[0]),Q[0]) % p
    y = check(mnoz(m, check(P[0],x)),P[1]) % p
    return(a, b, p, x1, y1, x2, y2,x,y)
