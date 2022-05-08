a=[2,3,4,[6,7,8],[7,3,6,3],6]
b=[]
i=0
while i<len(a):
    j=0
    while j<len(a[i]):
        if type(a[j])==list:
            pass
        else:
            b.append(a[i])
            j=j+1
        i=i+1    
print(b)        
        
        
# my_list = [[1], [2, 3], [4, 5, 6, 7]]
# k= sum(my_list, [])
# print(k)  



    