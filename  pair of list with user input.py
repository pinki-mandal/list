size=int(input("enter the  size of number"))
a=[]
i=0
j=0
for i in range(size):
    val=int(input("enter the number"))
    a.append(val)
for j in range(size):
    for j in range(0,size-i-1):
        if a[j]>a[j+1]:
            t=a[j]
            a[j]=a[j+1]
            a[j+1]=t
print("sorted array") 
print(a)           
 