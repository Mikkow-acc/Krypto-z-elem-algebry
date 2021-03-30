def rev(a): #Funckja do odwracania ciągów binarnych
    a.reverse()
    return a
def bintodec(a): #Funkcja do zamiany z zapisu binarnego na decymalny
    rev(a)
    sum = 0
    for i in range(len(a)):
        if a[i] == 1:
            sum+=2**i
    return sum
def dectobin(n): #Funkcja do zamiany z zapisu decymalnego na binarny
    binary = []
    while n != 0:
        bit = n % 2
        binary.append(bit)
        n = n // 2
    return rev(binary)
def exgcp(a,b): #Funkcja do obliczania NWD
    r,r1=bintodec(a),bintodec(b)
    s,s1=1,0 #sa+tb == a
    t,t1=0,1 #s1a+t1b == b
    while not(r1==0):
        q,r2=r//r1,r % r1
        r,s,t,r1,s1,t1=r1,s1,t1,r2,s-s1*q,t-t1*q
    d=r
    return d,s,t #sa+tb=d, d=GCD(a,b)

def miltInver(a,n): #Funckja do obliczania odwrotności modulo n
    (d,inv,_)=exgcp(a,n)
    if inv < 0:
        inv*=-1
    if d==1:
        if n==1:
            return 1
        return dziel(dectobin(inv),n)
    else:
        raise NameError('Numbers '+str(a)+' and '+str(n)+' are not comprime.')


def rozloz(n): #Funkcja rozkłądająca liczbę na czynniki pierwsze
    czynniki = []
    k = 2
    while n != 1:
        while n % k == 0:
            n //= k
            czynniki.append(k)
        k += 1
    return czynniki

def issqrof(p,a): #Funkcja sprawdzająca czy reszta modulo p jest kwadratem
    if exgcp(p,a)[0] == 1:
        p=bintodec(p)
        a = bintodec(a)
        prime = rozloz(a)
        sum = 1
        for i in prime:
            if i == 2:
                sum*=(-1**(((p**2)-1)/8))
            else:
                sum*=(-1**(((p-1))/2*((i-1)/2)))
        if sum == 1:
            print("tak")
        else:
            print("nie"
    else:
        raise NameError("Liczby nie sa wzglednie pierwsze")
p=[1, 0, 1, 0, 1, 1, 1, 1, 0, 1]
a=[1, 0, 0, 1, 0, 0, 0, 0, 0]
print(issqrof(p,a))