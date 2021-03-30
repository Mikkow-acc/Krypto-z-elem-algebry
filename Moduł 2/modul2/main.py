def Q(x,y):
    return x//y, x%y
def rev(a):
    a.reverse()
    return a
def modify(r):
    return list(map(int, "".join(list(map(str, r[::-1]))).lstrip("0")))
def bintodec(a):
    a = a[::-1]
    sum = 0
    for i in range(len(a)):
        if a[i] == 1:
            sum+=2**i
    return int(sum)
def dectobin(n):
    binary = []
    while n != 0:
        bit = n % 2
        binary.append(bit)
        n = n // 2
    return rev(binary)


def dodaj(a,b):
    a = dectobin(a)
    b = dectobin(b)
    if len(a) < len(b):
        pom = a
        a = b
        b = pom
    a = a[::-1]
    b = b[::-1]
    d=0
    ans=[]
    for i in range(len(b)):
        tmp = a[i]+b[i]+d
        d = Q(tmp,2)[0]
        ans.append(Q(tmp,2)[1])
    for i in range(len(b),len(a)):
        tmp = a[i]+d
        d = Q(tmp,2)[0]
        ans.append(Q(tmp,2)[1])
    ans.append(d)
    ans = rev(ans)
    if ans[0] == 0:
        ans = ans[1:]
    return bintodec(ans)
def check(a,b):
    if a == 0 and b == 0:
        return 0
    elif a >= 0 and b >= 0:
        if a < b:
            pom = a
            a = b
            b = pom
            return -1 * odejmij(a, b)

        return odejmij(a, b)
    elif a < 0 and b > 0:
        a *= a
        return dodaj(a,b)*-1
    elif a > 0 and b <0:
        b *= b
        return dodaj(a, b)
    elif a < 0 and b <0:
        a *= a
        b *= b
        if a < b:
            pom = a
            a = b
            b = pom
            return odejmij(a, b)
        return odejmij(a, b)*-1
def odejmij(a,b):
    if isinstance(a, int):
        if a < b:
            pom = a
            a = b
            b = pom
        a = dectobin(a)
        b = dectobin(b)
        a = a[::-1]
        b = b[::-1]

        result = [0] * len(a)


        for i in range(len(b)):

            if (a[i] == 0 and b[i] == 0) or (a[i] == 1 and b[i] == 1):
                result[i] = 0

            elif a[i] == 1 and b[i] == 0:
                result[i] = 1

            elif a[i] == 0 and b[i] == 1:
                j = i + 1
                a[i] = 2
                while a[j] == 0:
                    a[j] = 1
                    j += 1
                a[j] = 0
                result[i] = a[i] - b[i]
        for i in range(len(b), len(a)):
            result[i] = a[i]
        return bintodec(result[::-1])
    else:
        if len(a) < len(b):
            pom = a
            a = b
            b = pom
        a = a[::-1]
        b = b[::-1]
        d = 0
        ans = []
        for i in range(len(b)):
            tmp = a[i] - b[i] + d
            d = Q(tmp, 2)[0]
            ans.append(Q(tmp, 2)[1])
        for i in range(len(b), len(a)):
            tmp = a[i] - d
            d = Q(tmp, 2)[0]
            ans.append(Q(tmp, 2)[1])
        ans.append(d)
        ans = ans[::-1]
        while ans[0] != 1:
            ans.pop(0)
            if len(ans) == 0:
                break
        return (ans)

def dodcheck(a,b):
    if a<0 and b >0:
        a=a*-1
        return check(b,a)

def mnoz(a, b):
    # print(a,b)
    if not isinstance(a, int):
        if a == "0" or b == "0":
            return 0

        a = a[::-1]
        b = b[::-1]

        result = []
        for i in range(len(b) + len(a)):
            result.append(0)
        for i in range(len(a)):
            c = 0
            for j in range(len(b)):
                tmp = a[i] * b[j] + result[i + j] + c
                (c, result[i + j]) = Q(tmp, 2)
            result[i + len(b)] = c
        return result[::-1]
    else:
        if a < 0:
            a = a*-1
        if b < 0:
            b = b*-1
        a = dectobin(a)
        b = dectobin(b)
        if a == "0" or b == "0":
            return 0

        a = a[::-1]
        b = b[::-1]

        result = []
        for i in range(len(b) + len(a)):
            result.append(0)
        for i in range(len(a)):
            c = 0
            for j in range(len(b)):
                tmp = a[i] * b[j] + result[i + j] + c
                (c, result[i + j]) = Q(tmp, 2)
            result[i + len(b)] = c
        return bintodec(result[::-1])

def modify(r):
    return list(map(int, "".join(list(map(str, r[::-1]))).lstrip("0")))

def dziel(a, b):
    a = dectobin(a)
    b = dectobin(b)
    if not isinstance(a, int):
        a = a[::-1]
        b = b[::-1]

        r = []
        q = []

        for i in range(len(a) - len(b), -1, -1):
            q.append(0)

        for i in range(len(a)):
            r.append(a[i])
        r.append(0)

        for i in range(len(a) - len(b), -1, -1):
            q[i] = (r[i + len(b)] * 2 + r[i + len(b) - 1]) // b[len(b) - 1]
            if q[i] >= 2:
                q[i] = 1
            c = 0
            for j in range(len(b)):
                tmp = r[i + j] - q[i] * b[j] + c
                (c, r[i + j]) = Q(tmp, 2)
            r[i + len(b)] = r[i + len(b)] + c
            while r[i + len(b)] < 0:
                c = 0
                for j in range(len(b)):
                    tmp = r[i + j] + b[j] + c
                    (c, r[i + j]) = Q(tmp, 2)
                r[i + len(b)] = r[i + len(b)] + c
                q[i] = q[i] - 1
        return bintodec(modify(q)), bintodec(modify(r))
    else:
        if a < 0:
            a=a*-1
        if b < 0:
            b=b*-1
        a = dectobin(a)
        b = dectobin(b)
        a = a[::-1]
        b = b[::-1]

        r = []
        q = []

        for i in range(len(a) - len(b), -1, -1):
            q.append(0)

        for i in range(len(a)):
            r.append(a[i])
        r.append(0)

        for i in range(len(a) - len(b), -1, -1):
            q[i] = (r[i + len(b)] * 2 + r[i + len(b) - 1]) // b[len(b) - 1]
            if q[i] >= 2:
                q[i] = 1
            c = 0
            for j in range(len(b)):
                tmp = r[i + j] - q[i] * b[j] + c
                (c, r[i + j]) = Q(tmp, 2)
            r[i + len(b)] = r[i + len(b)] + c
            while r[i + len(b)] < 0:
                c = 0
                for j in range(len(b)):
                    tmp = r[i + j] + b[j] + c
                    (c, r[i + j]) = Q(tmp, 2)
                r[i + len(b)] = r[i + len(b)] + c
                q[i] = q[i] - 1
        return bintodec(modify(r)),bintodec(modify(q))

def poteg(b, k, n):
    ifbin = False
    if not isinstance(b, int):
        b = bintodec(b)
        k = bintodec(k)
        n = bintodec(n)
        ifbin = True
    k_binary = f"{k:b}"
    length = len(k_binary) - 1
    index = 0
    tmp = 1

    while length >= 0:
        tmp = tmp * tmp % n
        if str(k_binary)[index] == str(1):
            tmp = (tmp*b) % n
        index += 1
        length = length - 1
    if ifbin == True:
        return dectobin(tmp)
    elif ifbin == False:
        return tmp


def exgcp(a,b):
    r,r1=bintodec(a),bintodec(b)
    s,s1=1,0
    t,t1=0,1
    while not(r1==0):
        q,r2=r//r1,r % r1
        r,s,t,r1,s1,t1=r1,s1,t1,r2,s-s1*q,t-t1*q
    d=r
    return d,s,t

def miltInver(a,n):
    (d,inv,_)=exgcp(a,n)
    if inv < 0:
        inv*=-1
    if d==1:
        if n==1:
            return 1
        return dziel(dectobin(inv),n)
    else:
        raise NameError('Numbers '+str(a)+' and '+str(n)+' are not comprime.')

def rozloz(n):
    czynniki = []
    k = 2
    while n != 1:
        while n % k == 0:
            n //= k
            czynniki.append(k)
        k += 1
    return czynniki

def issqrof(p,a):
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
            print("nie")
    else:
        raise NameError("Liczby nie sa wzglednie pierwsze")

def faktor(x):
    fact = []
    iloraz = 1
    for i in range(1, x + 1):
        if x % i == 0:
            iloraz*=i
            fact.append(i)
            if iloraz==x:
                break
    stri = ''
    for x in fact[1:]:
        stri+= str(x) + ' * '
    stri = stri[:-2]
    return stri

def fermat(a,n):
    a = dectobin(a)
    n = dectobin(n)
    b = odejmij(n,[1])
    x = poteg(a, b, n)
    try:
        if not(x==1):
            return 'tak'
        else:
            return 'nie'
    except: print("Toomuch")
