# ch=input("enter the alphabet")
# if ch>"A"or"a" and  ch<"z"or"Z":
#     print(ch,"alphabet")
#     n=int(input("enter the number"))
#     if n>1 or n<10:
#         print(n,"number")
#         s=input("enter the special character")
#         if "@" or "#":
#             print(s,"special character")
#             password=ch+str(n)+s
#             print(password)
#             print("strong password")
#         else:
#             print("not") 
#     else:
#         print("nothing")   
# else:
#     print("never")    


# a=input("enter:")
# b=a[-1::-1]
# if a==b:
#     print("palidrom")
# else:
#     print("no")   


   
# row=0
# while row<6:
#     coloum=0
#     while coloum<7:
#         if (row==0 and coloum%3!=0) or (row==1 and coloum%3==0) or (row-coloum==2) or (row+coloum==8):
#             print("*",end="  ")
#         else:
#             print(end="  ") 
#         coloum=coloum+1
#     print() 
#     row=row+1   




# a=int(input("enter the number"))
# b=int(input("enter the number"))
# c=int(input("enter the number"))
# if a>b and a>c:
#     print("a is greater")
# elif b>a and b>c:
#     print("b is greater")
# elif c>a and c>b:
#     print("c is greater")
# else:
#     print("nothing")            
    



# x = "global"
# def foo():
#     print("x inside:", x)
# foo()
# print("x outside:", x)    



# def foo():
#     y = "local"
# foo()
# print(y)       