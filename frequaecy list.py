char_list ="MISSISSIPPI"
i=0
a=[]
while i<len(char_list):
    j=0
    b=[]
    count=0
    while j<len(char_list):
        if char_list[i] in char_list:
            if char_list[i]==char_list[j]:
                count=count+1
        j=j+1
    b.append(char_list[i]) 
    b.append(count)  
    if b not in a:
        a.append(b) 
    i+=1
print(a)


