def Q(x,y):
    return x//y, x%y
def rev(li):
    tmp=li
    tmp.reverse()
    return tmp
def dod(a,b):
    rev(a)
    rev(b)
    c = 0
    ans = []
    for i in range(0,len(b)):
        temp = a[i]+b[i]+c
        c = Q(temp,2)[0]
        ans.append(Q(temp,2)[1])
    for i in range(len(b),len(a)):
        temp = a[i]+c
        c,ans = Q(tmp,2)
    ans.append(c)
    print(rev(ans))
    
a = [1,0,1,1,1,0,0]
b = [1,0,1,0,0,1,1]
dod(a,b)