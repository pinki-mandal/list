print(".*.*.*.*kaun banega crorepati*.*.*.*")
question_list=["how many continent are there?",
        "Which is the capital of india?",
        "ng mei kaun se course padhaya jata hai?",
        " who founded microsoft"]
        
options_list=[
        ["four","nine","seven","eight"],
        ["chandigarh","bhopal","chennai","delhi"],
        ["software engineering","counseling","tourism","agriculture"],
        ["elon musk","jeff","mark","bill gates"]]
solution_list=[3,4,1,2]   
answer=[["2.nine","3.seven"],
        ["3.chennai","4.delhi"],
        ["2.counseling","1.software engineering"],
        ["2.jeff","4.bill gates"]]
print(".*.*.*kbc*.*.*.*.")
i=0
s=0
count=0
while i<len(question_list):
    print(question_list[i])
    a=0
    b=i
    while a<len(options_list[i]):
        k=options_list[i][a]
        print(a+1,k)
        a+=1
    num=input("do you want 50 50 lifeline yes/no") 
    if num=="yes":
        print("accept") 
        if count<1:
            print(answer[b])
            num1=int(input("enter the answer")) 
            if num1==solution_list[i]:
                s+=1
                print("your answer is correct") 
                print("you win  rs/",s)
            else:
                print("incorrect answer") 
                print("you win rs/",s) 
                break
            count+=2000
        else:
            print("you  already use lifeline") 
            num2=int(input("enter the answer"))   
            if num2==solution_list[i]:
                print("congrats your answer is right") 
                s+=10
                print("you win rs/",s) 
            else:
                print("your answer is wrong")  
                print("you win rs/",s) 
                break
    else:
        pass
        k=int(input("enter the anser")) 
        if k==solution_list[i]:
            print("right answer") 
            s+=1000
            print("you win rs/",s)
        else:
            print("no chance") 
            print("your answer is wrong")  
            print("you win rs/",s) 
    i=i+1   
print("conguratulation.... you participate in kbc game")
print("you win rs/",s)  
print("thanks for participating......")     
             