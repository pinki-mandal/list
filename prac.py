# a=["a","b","c","d"]
# b=["g","h","i","d"]
# i=0
# while i<len(a):
#     c=a[i]+b[i]
#     i=i+1
#     print(c)    

 

# a=["a","b","c","d"]
# b=["g","h","i","d"]
# i=0
# c={}
# while i<len(a):
#     h=a[i]+b[-i]
#     c.update({i:h})
#     i=i+1
# print(c)    

# a=["a","b","c","d"]
# b=["g","h","i","d"]
# i=0
# c={}
# while i<len(a):
#     h=a[i]+b[-i]
#     c.update({i:h})
#     i=i+1
# print(c)

# a=[["aa"],["aaa"],["aaaa"]]
# max=0
# i=0
# while i<len(a):
#     if max<a[i]:
#         max=a[i]
#         i=i+1
#     print(max)    







# a=["pooja","sona","jayashree"]
# i=0
# c=0
# s=[]
# while i<len(a):
#     if len(a[i])%2==0:
#         print(a[i],"even")
#         s.append(a[i])
#         # c+=1
        
#     else:
#         print(a[i],"odd") 
#         s.append(a[i])
#         # c+=1
#     i=i+1
# print(s)    
# # print(c)           
    
    
    
    
    
    
# a=[5,8,7,15,25,35] 
# i=0
# b=[]   
# c=[]
# while i<len(a):
#     if a[i]%5==0:
#         # print(a[i],"yes")
#         b.append(a[i])
#     else:
#         c.append(a[i])
#         # print(a[i],"no")
#     i=i+1
# print(b)            
# print(c)



# a={12:3,4:8,6:9,0:7}
# count=1
# for i in a:
#     if a[i]%2==0:
#         count=count+1
#     if count==2:
#         print(i,"it is not prime no") 
#     else:
#         print(a[i],"it is a prime no")       




# a=["pinki","mandal"]  
# i=0
# list=[]
# while i < len(a):
#     j=0
#     while j< len(a[i]):
#         s=(a[i][0])
#         j+=1
#     list.append(s)  
#     i+=1
# print(list)




# a=[1,2,3,4,5,6,7,8,9,10]
# i=0
# sum=0
# pro=1
# while i<len(a):
#     if i<=5:
#         sum=sum+i
#     else:
#         pro=pro*i
#     i=i+1
# print(sum)
# print(pro)


# a=[1,2,3,4,5,6]
# i=0
# m=[]
# while i<len(a):
#     if i<=5:
#         m.append(a[i])
#     i=i+1
# print(m) 
       
        




# a=[1,2,0,6,7,0,2,3,0]
# i=0
# m=[]
# while i<len(a):
#     if (a[i]==0):
#         pass
#     else:
#         m.append(a[i])
#     i=i+1
# print(m)          



# txt = "I like bananas"
# x = txt.replace("bananas", "apples")
# print(x) 



# a=[1,2,0,4,5,0,6,0]


# def convertRec(no):  
#     if(no==0): 
#        return 0
#     digit=no%10
#     if(digit==0): 
#         digit=5 
#     return int(convertRec(no//10))*10+digit
# def convert(no): 
#     if(no==0): 
#         return 5
#     else: 
#         return convertRec(no)  
# no=int(input("Enter the integer:"))
# print("Converted integer:",convert(no))





# n=[1,0,2,0,5,0,0]
# n=str(n)
# n2=n.replace('0','5')
# print("Converted number:",n2)





# l = [1, 2, [3, 4, [5, 6]], 7, 8, [9, [10]]]
# m= []
# def number(l):
#     for i in l:
#         if type(i) == list:
#             number(i)
#         else:
#             m.append(i)
# number(l)
# print ('The list after removing nesting: ',m)



# a= ["a","b","c","d"]
# s= []
# for i in a:
#    m= i.split(', ')
#    s.append((m))
# k= []

# for i in s:
#     m = []
#     for e in i:
#         m.append(e)
#     k.append(m)

# print(k)

