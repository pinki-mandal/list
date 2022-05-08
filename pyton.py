a=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
num=int(input("enter the number")) 
size=int(input("enter the size"))
i=1
b=[]        
while i<len(a):
    j=1
    if i<size:
        j=num*i
        b.append(j) 
    i=i+1  
    
print(b) 




# a=[4,5,6,2,3,8,7,6]
# i=0
# b=[]
# while i<len(a):
#     count=0
#     j=0
#     while j<len(a):
#         if a[i]<a[j]:
#             count+=1
        
#         j+=1
#     b.append(count)
#     i+=1
# print(b)










# a=[[1,2,3],[1,2,3]]
# i=0
# b=[]
# while i<len(a):
#     j=0
#     sum=0
#     while j<len(a[i]):
#         sum=sum+a[i][j]
#         j=j+1
#     b.append(sum)
#     i=i+1
# print(b)        
        
                                                                                                                                         