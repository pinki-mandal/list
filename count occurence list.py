a=[]
x=int(input("enter max size  "))
for i in range(x):
    val=input("enter value")
    a.append(val)
z=input("enter value to count:")
y=a.count(z)
print(z,"appear in the list",y,"times")


1
2
3
4
5
6

	

# Shape and Reshape in Python - Hacker Rank Solution
# Python 3
import numpy
# Shape and Reshape in Python - Hacker Rank Solution START
print(numpy.array(input().split(), int).reshape(3, 3))
# Shape and Reshape in Python - Hacker Rank Solution END

 
