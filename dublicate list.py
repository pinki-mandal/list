# a= [1, 2, 3, 1, 2, 4, 5, 4 ,6, 2]
# d = []
# for i in a:
#     if i not in d:
#         d.append(i)
# a = d
# print("List After removing duplicates ",a)




# a=[5,6,7,8,5,6,8]
# d=[]
# i=0
# while i<len(a):
#     j=a[i]
#     if j not in d:
#         d.append(j)
#     i=i+1
# print(d)        


a=[7,3,7,4,5]
i=0
d=[]
while i<len(a):
    j=a[i]
    if j not in d:
        d.append(j)
    i+=1
print(d)        