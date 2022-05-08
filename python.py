a=[0, 10, [20, 30], 40, 50, [60, 70, 80], [90, 100, 110, 120]]
b=[]
i=0
while i<len(a):
    if type(a[i])==type(list):
        j=0
        while j<len(a[i]):
            b.append(a[i][j])
            j+=1
    else:
        b.append(a[i]) 
    i+=1
print(b)    
    
           
        