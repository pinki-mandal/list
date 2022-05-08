a=[4,5,6,[2,3,5],[6,8]]   
i=0
sum=0
b=[]
while i<len(a):
    if type(a[i])==list:
        pass
    else:
        b.append(a[i])
        sum=sum+a[i]
    i=i+1
print(sum)   