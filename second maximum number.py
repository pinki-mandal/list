# a=[20, 30, 40, 25, 10]  
# second_max=0
# i=0
# while i<len(a):
#     a.sort()
#     second_max+=i
#     i=i+1
# print("The second largest element of the list is:",a[-2])  
 
a=[5,6,7,8,3,2]
max=0
i=0
while i<len(a):
    if max<a[i]:
        max=a[i]
    i+=1
print(max)   
i=0
max1=0
while i<len(a):
    if max1<a[i]:
        if max!=a[i]:
            max1=a[i]
        i+=1
print(max1)                 