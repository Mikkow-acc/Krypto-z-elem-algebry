import random
from math import log, floor, sqrt
from random import randint
import ecli
def OppPt(p, x, y):
    return (x % p), (-1 * y % p)
def inv(p, x, y):
    return (x % p), (-1 * y % p)
def add_ellip(p, A, P, Q):
    z = 0

    if (P == z):
        return Q
    if (Q == z):
        return P

    if P[0] == Q[0]:
        if (P == (Q[0], -Q[1] % p)):
            return z
        else:
            m = ((3 * pow(P[0], 2, p) + A) * pow(2 * P[1], p - 2, p)) % p
    else:
        m = (P[1] - Q[1]) * pow(P[0] - Q[0], p - 2, p) % p

    x = (pow(m, 2, p) - P[0] - Q[0]) % p
    y = (m * (P[0] - x) - P[1]) % p
    return (x, y)


def pow2floor(x):
    p = 1
    x >>= 1
    while (x > 0):
        x >>= 1
        p <<= 1
    return p


def multi_nP(p, A, n, P):
    d = {}

    def rec_helper(n, P):
        sign = 1
        if (n == 0):
            return (0, 0)
        elif (n == 1):
            return P
        elif (n in d):
            return d[n]
        else:
            if n < 0:
                sign = -1
                n = n * -1
            p2f = pow2floor(n)
            remainder = n - p2f

            lower_half = rec_helper(p2f // 2, P)
            d[p2f // 2] = lower_half
            nP = add_ellip(p, A, lower_half, lower_half)

            if (remainder):
                nP = add_ellip(p, A, nP, rec_helper(remainder, P))

            d[n] = nP
            x1 = nP[0]
            x2 = nP[1]
            if sign == -1:
                x1, x2 = OppPt(p, x1, x2)
            return x1, x2
    return rec_helper(n, P)


# zad1 Algorytm implementujący szybkie dodawanie na krzywej eliptycznej
def MultPoint(p, A, B, P, n):
    Q = multi_nP(p, A, n, P)
    return A, B, p, P[0], P[1], Q[0], Q[1], n


# p = 157
# A = 138
# B = 68
# P = [25, 60]
# n = -130
# print(MultPoint(p,A,B,P,n))

# zad2 Algorytm generujący klucz publiczny i prywatny w protokole Elgamal
def ElgamalPubPrivateKey(k):
    p = ecli.gen(k)
    A, B = ecli.generate(p)
    P = ecli.random_point(A, B, p)
    if log(P[0], 2) > k / 4 and log(P[1], 2) > k / 4:
        x = random.randint(2, floor(p + 1 - (2 * p ** (1 / 2))))
        Q = multi_nP(p, A, x, P)
        priv = [A, B, p, P[0], P[1], Q[0], Q[1], x]
        pub = [A, B, p, P[0], P[1], Q[0], Q[1]]
        return 'k.pub',pub, 'k.priv',priv



# print(ElgamalPubPrivateKey(20))

# zad3 Algorytm kodujący i dekodujący wiadomość
def EncodeMessage(A, B, p, k, M):
    for n in range(1, k):
        x = M * k + n
        for y in range(0, p - 1):
            if (y ** 2) % p == ((x ** 3) + A * x + B) % p:
                return x, y
# print(EncodeMessage(226183941, 153555317, 1058172317, 100, 10430154))

def DecodeMessage(k,x):
    return (x) // k

# zad4 Algorytm szyfrujący metodą Elgamal
def encElgamal(A, B, p, xq, yq, xp, yp, M):
    xpm = ypm = M
    k = randint(1, int(p + 1 - 2 * sqrt(p)))
    xc1, yc1 = MultPoint(p, A, B, [xq,yq], k)[5:7]
    kpx, kpy = MultPoint(p, A, B, [xp,yp], k)[5:7]
    xc2, yc2 = add_ellip(p, A,[xpm, ypm], [kpx, kpy])
    return xc1, yc1, xc2, yc2
# print(encElgamal(615310606977377600, 368641938789887509, 630858080829889823, 30971916540155906, 256563467271589783, 48364257713943279, 607273520761100679, 6152992012277699))

#zad5 Algorytm deszyfrujący metodą Elgamal
def decElgamal(A, B, p,xQ,yQ,xP,yP,x,xc1, yc1, xc2, yc2):
    k = 100
    xxc1, yxc1 = MultPoint(p, A, B, [xc1,yc1], x)[5:7]
    xxc1, yxc1 = inv(p,xxc1, yxc1)
    Pm = add_ellip(p, A, [xc2, yc2], [xxc1, yxc1])
    M = DecodeMessage(k,Pm[0])
    return M
# print(decElgamal(326671493585, 160090973274, 537374646323, 355243422100, 510924546451, 536280978049, 202696759151, 145844796485, 168579421226, 74965911094, 103462075868, 166202062939))
