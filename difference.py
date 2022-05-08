# list1 = [1, 2, 4]
# list2 = [4, 5, 6]
# list_difference = []
# for item in list1:
#   if item not in list2:
#     list_difference.append(item)
# print(list_difference)







list1=[1,2,3,4,5,6] 
list2=[2,3,1,0,6,7]  
b=[] 
i=0
while i<len(list1):
    if i not in  list2:
        b.append(i)
    i+=1
print(b)        
        