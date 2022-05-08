ch=input("enter the alphabet")
if ch>"A"or"a" and  ch<"z"or"Z":
    print(ch,"alphabet")
    n=int(input("enter the number"))
    if n>1 or n<10:
        print(n,"number")
        s=input("enter the special character")
        if "@" or "#":
            print(s,"special character")
            password=ch+str(n)+s
            print(password)
            print("strong password")
        else:
            print("not") 
    else:
        print("nothing")   
else:
    print("never")                
           
           
 
        
    
