def dodaj(a,b): #Funkcja do dodawania liczb(input i output bin)
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
    return (ans)