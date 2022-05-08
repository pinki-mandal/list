# thisdic={"apple":2,"banana":3}
# values=thisdic.values()
# total=sum(values)
# print(total)

# # thisdic={"a":1,"b":2,"c":6}
# # values=thisdic.values()
# # total=sum(values)
# # print(total)   

# thisdic={"a":5,"b":3}
# values=thisdic.values()
# total=(values)
# print(total)

# a=[1,2,3,4,5]
# i=0
# sum=0
# while i<len(a):
#     sum=sum+a[i]
#     i=i+1
# print(sum)

# a=[2,3,5,1,4]
# max=0
# i=0
# while i<len(a):
#     if max<a[i]:
#         max=a[i]
#     i=i+1
# print(max)  
# i=0
# max1=0
# while i<len(a):
#     if max1<a[i]:
#         if max!=a[i]:
#             max1=a[i] 
#     i=i+1
# print(max1)   
# i=0
# max2=0
# while i<len(a):
#     if max2<a[i]:
#         if max1!=a[i] and max!=a[i]:
#             max2=a[i] 
#     i=i+1
# print(max2)                   
        
# a=[4,5,6,7,8]        
# i=0
# while  i<len(a):
#     j=0
#     while j<len(a)-1:
#         if a[i]<a[j]:
#             c=a[i]
#             a[i]=a[j]
#             a[j]=c
#         j=j+1
#     i=i+1
# print(a)            

# a=[4,5,6,7,8]        
# i=0
# while  i<len(a):
#     j=0
#     while j<len(a)-1:
#         if a[i]>a[j]:
#             c=a[i]
#             a[i]=a[j]
#             a[j]=c
#         j=j+1
#     i=i+1
# print(a)      

# a=[5,6,7,[4,5,6],6]
# i=0
# sum=0
# while i<len(a):
#     if type(a[i])==list:
#         pass
#     else:
#         sum=sum+a[i]
#     i=i+1
# print(sum)        
        
# a=[5,6,7,[4,5,6],6]
# i=0
# sum=0
# while i<len(a):
#     if type(a[i])==list:
#         pass
#     else:
#         sum=sum+a[i]
#     i=i+1
# print(sum)        
        
        
        
        
# a=[5,6,7,[4,5,6],6]
# i=0
# while i<len(a):
#     if type(a[i])==list:
#         j=0
#         sum=0
#         while j<len(a[i]):
#             sum=sum+a[i][j]
#             j=j+1
#     i=i+1
# print(sum)        



a=[5,6,7,[2,3,4,[5,6,7]]]
i=0
while i<len(a):
    if type(a[i])==list:
        j=0
        sum=0
        while j<len(a[i]):
            sum=sum+a[i][j]
            j=j+1
    else:
        sum=sum+a[i]
    i=i+1
print(sum)        
    
    
    
    
    
                
# a={4+5}                
# print(a)




# my_dict = {'C1':[1,2,3],'C2':[5,6,7],'C3':[9,10,11]}
# for row in zip(*([key] + (value) for key, value in sorted(my_dict.items()))):
#     print(*row)








# d=[{'item': 'item1', 'amount': 400}, {'item': 'item2', 'amount': 300}, {'item': 'item1', 'amount': 750}]
# d1={}
# for i in d:
#     if i['item'] in d1.keys():
#         d1[i['item']]+=i['amount']
#     else:
#         d1[i['item']]=i['amount']
# print(d1)


        


# current=int(input("enter the number"))
# birth=int(input("enter the number"))
# age=current-birth
# if current-birth:
#     print(age)




# a= [1,2,3,4]
# b={}
# c={}
# b=c
# for i in a:
#     c[i]={}
#     c=c[i]
# print(b)
 
 
 


# d = {'1':['a','b'], '2':['c','d']}
# for i in d:
#     for j in d:
#         print(i+j)



# l = [{'id': '#FF0000', 'color': 'Red'}, {'id': '#800000','color': 'Maroon'}, {'id': '#FFFF00', 'color': 'Yellow'},{'id': '#808000', 'color': 'Olive'}]
# b= []
# for i in l:
#     if (i['id'] != '#FF0000'):
#         b.append(i)
# print(b) 









    
    




