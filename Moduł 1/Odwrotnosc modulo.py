def Q(x,y):
    return x//y, x%y
def rev(a):
    a.reverse()
    return a
def dodaj(a,b):
    if len(a)<len(b):
        pom = a
        a = b
        b = pom
    a = rev(a)
    b = rev(b)
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
    if ans[0]==0:
        ans = ans[1:]
    return(ans)

def odejmij(a,b):
    if len(a)<len(b):
        pom = a
        a = b
        b = pom
    a = rev(a)
    b = rev(b)
    d=0
    ans=[]
    for i in range(len(b)):
        tmp = a[i]-b[i]+d
        d = Q(tmp,2)[0]
        ans.append(Q(tmp,2)[1])
    for i in range(len(b),len(a)):
        tmp = a[i]-d
        d = Q(tmp,2)[0]
        ans.append(Q(tmp,2)[1])
    ans.append(d)
    print(rev(ans))

def mnoz(a,b):
    # if len(a)<len(b):
    #     pom = a
    #     a = b
    #     b = pom
    a = rev(a)
    b = rev(b)
    ans=[]
    for i in range(len(a)+len(b)):
        ans.insert(i,0)
    for i in range(len(a)):
        d=0;
        for j in range(len(b)):
            tmp=a[i]*b[j]+ans[i+j]+d
            d = Q(tmp,2)[0]
            (d, ans[i+j]) = Q(tmp,2)
        ans[i+len(b)] = d
    ans = rev(ans)
    if ans[0] == 0:
        ans = ans[1:]
    return (ans)

def dziel(a,b):
    a = rev(a)
    b = rev(b)
    r=[]
    q=[]
    for i in range(len(a)):
        r.append(a[i])
    r.append(0)
    x=len(a)-len(b)
    for i in range(x,-1,-1):
        q.append(0)
    for i in range(x,-1,-1):
        q[i]=(((r[i+len(b)])*2+(r[i+len(b)-1]))//b[len(b)-1])
        if q[i]>=2:
            q[i]=2-1
        d=0
        for j in range(len(b)):
            tmp = r[i+j]-(q[i]*b[j])+d
            (d,r[i+j]) = Q(tmp,2)
        r[i+len(b)]=r[i+len(b)]+d
        while r[i+len(b)]<0:
            d=0
            for j in range(len(b)):
                tmp = r[i+j] + b[j] + d
                (d,r[i+j]) = Q(tmp,2)
            r[i+len(b)] = r[i+len(b)]+d
            q[i]=q[i]-1
    rev(r)
    while r[0] != 1:
        r.pop(0)
        if len(r) == 0:
            break
    return rev(q), r

def bintodec(a):
    rev(a)
    sum = 0
    for i in range(len(a)):
        if a[i] == 1:
            sum+=2**i
    return sum
def dectobin(n):
    binary = []
    while n != 0:
        bit = n % 2
        binary.append(bit)
        n = n // 2
    return rev(binary)
# Declaration of ExtendedGCP
def exgcp(a,b):
    r,r1=bintodec(a),bintodec(b)
    s,s1=1,0 #sa+tb == a
    t,t1=0,1 #s1a+t1b == b
    while not(r1==0):
        q,r2=r//r1,r % r1
        r,s,t,r1,s1,t1=r1,s1,t1,r2,s-s1*q,t-t1*q
    d=r
    return d,s,t #
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

a=[1, 0, 0, 1, 1, 0, 1, 0, 1, 1]
b=[1, 0, 1, 1, 1, 1, 0, 0, 0, 1]
d=exgcp(a,b)[0]
inv=miltInver(a,b)[1]
print(dectobin(d),inv)
