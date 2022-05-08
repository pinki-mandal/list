# num=int(input('ente'))
# i=2
# while i<num:
#     if (num%1==0):
#         print(num,"prime not")
#     break
# else:
#         print(num,"prime")
# i=i+1        

num=int(input("enter the number"))
i=0
while i<num:
    if num%1==0 or num==2 or num%num==0:
        print("prime number")
    else:
        print("not prime number")       