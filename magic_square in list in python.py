r=int(input("enter the number of rows:"))
c=int(input("enter the number of coloum:"))
magic_square=[]
print("enter the entries rowwise:")
for i in range(r):
    a=[]
    for j in range(c):
        a.append(int(input()))
    magic_square.append(a) 
for i in range(r):
    for j in range(c):
        print(magic_square[i][j],end="") 
    print()   
