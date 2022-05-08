a=[[2,3,4],[5,6,7,8],[7,6,],[9,8,7]]
i=0
while i<len(a):
    j=0
    while a[j]<a[i]:
        j+=1
    i+=1
print(a[j])
