
a=[12,34,56]
add=[]
for ele in a:
    sum=0
    for digit in str(ele):
        sum+=int(digit)
    add.append(sum)   
print("list integer"+str(add))   
 
