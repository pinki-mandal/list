a=[1,2,"pinky","rupa",56,7]
count=0
i=0
while i<len(a):
    if type (a[i])==str:
        count=count+1
    i=i+1
print(count)    
