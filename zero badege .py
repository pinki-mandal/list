n=int(input("enter the number"))
a=list(str(n))
m=len(a)
l=m-1
i=0
while i<len(a) and i<l:
    k=int(a[i])
    v=(k)*10**l
    print(v,end=" ")
    if i!=len(a):
        print("+",end=" ")
    l=l+1
    i=i+1    



