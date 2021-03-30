def mnoz(a,b): #Funkcja do mnożenia liczb(input i output bin)
    a = a[::-1]
    b = b[::-1]
    ans=[]
    for i in range(len(a)+len(b)):
        ans.append(0)
    for i in range(len(a)):
        d=0;
        for j in range(len(b)):
            tmp=a[i]*b[j]+ans[i+j]+d
            (d, ans[i+j]) = Q(tmp,2)
        ans[i+len(b)] = d
    ans = rev(ans)
    while ans[0] != 1:
        ans.pop(0)
        if len(ans) == 0:
            break
    return(ans)