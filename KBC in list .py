question_list=["Which festival is called the festival of light?",
        "Which is the capital of india?",
        "Which is the tallest animal on the earth?",
        "Which is the largest animal in the world",
        "What Type of bird lays the largest eggs"]
        
options_list=[
        ["holi","durrehra","rakhsha bandhan","diwali"],
        ["Delhi","Agra","Himachal","Shimla"],
        ["lion","Giraffe","Deer","Blue whale"],
        ["lion","Blue whale","Monkey","panda"],
        ["Parrot","Crow","Ostrich","Peacock"],
        ] 
solution_list=["A","B","A","B"]
answer=["holi","diwali"],["delhi","agra"],["lion","girrafe"],["blue whale","deer"],["crow","ostrich"]
i=0
while i<len(question_list):
    print(i+1,question_list[i])
    count=0
    j=i
    serial_no=0
    while serial_no<len(options_list[i]):
        k=(options_list[j][serial_no])
        print(serial_no+1,k)
        serial_no+=1
    num=input("enter the answer")
    if num=="diwali" or num=="delhi" or num=="girrafe" or num=="blue whale" or num=="ostrich":
        print("right answer")
    else:
        print("wrong answer")
        break
    i=i+1
    


