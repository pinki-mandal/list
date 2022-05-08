a=int(input("Enter size:"))
b=1
c=[]
while b<=a:
    n=int(input("Enter number:"))
    c.append(n)
    b=b+1
print(c)
i=0
while i<len(c):
    rem=(c[i]//10)%10
    b=c[i]//100
    sum=b*100
    sum1=rem*10 
    rem3=c[i]%10
    i=i+1
    print(sum,'+',sum1,'+',rem3)  
    
