a=[1,2,3,4,5,6]
i=0
max=0
while i<len(a):
    if max<a[i]:
        max=a[i]
    i=i+1
print("greater number",max) 
i=0
max1=0
while i<len(a):
    if max1<a[i]:
        if max!=a[i]:
            max1=a[i]
    i=i+1
print("second greater number",max1) 
i=0
max2=0
while i<len(a):
    if max2<a[i]:
        if max1!=a[i] and max!=a[i]:
            max2=a[i]  
    i=i+1
print("third greater number",max2)                  
