a=[[4,5,6],[7,8,9]] 
i=0
min=a[i] 
while i<len(a):
    j=0
    while j>len(a[i]):
        if  min>a[i]:
            min=a[i] 
        j=j+1
    i=i+1
print(min) 


   

# a=[5,6,7,3,2]
# i=0
# while i<len(a):
#     print(a[i])
#     i+=1
     
     
# a=[3,4,5,7,8]
# pro=1
# i=0
# while i<len(a):
#     if a*2:
#         pro=pro*a[i]
#     i+=1
# print(pro) 
# pro=pro+1       

# a=[3,4,9,6,7]
# i=0
# min=a[i]
# while i<len(a):
#     if min>a[i]:
#         max=a[i]
#     i+=1
# print(min)    
        
        
        
# a=[5,6,7,82,5,6,7]        
# b=[]
# i=0
# while i<len(a):
#     if a[i] not in b:
#         b.append(a[i])
#     i+=1
# print(b)        


# a=[3,4,5,6,7,8,8]
# i=0
# max=0
# while i<len(a):
#     if max<a[i]:
#         max=a[i]
#     i+=1
# print(max)        
# i=0
# max1=0
# while i<len(a):
#     if max!=a[i]:
#         if max1<a[i]:
#             max1=a[i]
#     i+=1
# print("second maximum",max1)    






# a=[50,40,23,70,56,12,5,10,7]
# i=0
# while i<len(a):
#     if a[i]>20 and a[i]<40:
#         print(a[i])
#     i+=1    




# a=[4,5,6,7] 
# pro=1
# i=0
# while i<len(a):
#     pro=pro*a[i]
#     i+=1
# print(pro)    


# a=[4,5,6,[3,4,5,6]]
# i=0
# b=[]
# while i<len(a):
#     if type(a[i])==list:
#         j=0
#         while j<len(a[i]):
#             b.append(a[i][j])
#             j+=1
#     else:
#         b.append(a[i])        
#     i+=1
# print(b)        
            
        
# a=[2,3,[6,7,8,9],[2,3,4,5]]
# i=0
# n=[]
# while i<len(a):
#     if type(a[i])==list:
#         j=0
#         while j<len(a[i]):
#             n.append(a[i][j])
#             j=j+1
#     else:
#         n.append(a[i])
#     i=i+1
# print(n)          


# a=[4,5,2,6,2,1]
# max=0
# i=0
# while i<len(a):
#     if max<a[i]:
#         max=a[i]
#     i+=1
# print(max)        