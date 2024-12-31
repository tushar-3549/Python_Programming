#Basic1
#q1

import datetime
now=datetime.datetime.now()
print("Current Date and Time :")
print(now.strftime("%Y-%m-%d \n%H:%M:%S"))

#q2
values=input("Enter Elements:")
li=values.split(",")
tup=tuple(li)
print("List: ",li)
print("Tuple: ",tup)

#q3
exam_date=(11,12,2021)
print("The examination will start from : %i / %i / %i" %exam_date)


#Ramdom number

from random import randint
guess = int(input("Enter a number between 1 to 5 : "))
RandomNumber = randint(1,5)

if guess==RandomNumber:
    print("You are win the game !")
else:
    print("You're lose at the game !")
    print("The guessing number was : ",RandomNumber)

#list as input from user

n=input("Enter a text of numbers : ")
list=n.split()
sum=0
for i in list:
    sum=sum+int(i)
print(sum)

#Matrix

matrix=[
        [1,2,3],
        [4,5,6]
        
        ]
print(matrix[0][2])

#xargs
def student(*details):
    print(details)
    
student(101,"Tushar")
student(102,"Maruf")

# -> it works just like tuple
def add(*numbers):
    sum=0
    for i in numbers:
        sum=sum+i
    print(sum)
    
add(10,20)
add(30,40,50)

#xxargs -> It works like dictionary

def student(**details):
    print(details)
student(ID=101,Name="Tushar")

#Lamda Function : A func without name(Anonymous func)

ans = (lambda a,b:a*a+2*a*b+b*b)(2,3)
print(ans)

#map
def cube(x):
    return x*x*x
num=[1,2,3,4,5]
res = list(map(cube,num))
print(res)

#filter
num=[1,2,3,4,5]
res=list(filter(lambda x:x%2==0, num))
print(res)

#List comprehensive 
num = [1,2,3,4,5]
res = [x*x for x in num]
print(res)

#zip
name=["Tushar","Maruf","Sakib","Roman"]
id=[10,12,13,45]
res=list(zip(name,id))
print(res)

#swap
a=10
b=20
a,b=b,a
print("Value of a : ",a)
print("Value of b : ",b)

#sorting 
num=[1,4,7,3,9,5,8,6]
#num.sort()
num.sort(reverse=True)
print(num)

#set
num1={1,2,3,4,4,5}
print(num1)
num2=set([6,6,7,8,9])
num2.add(11)
num2.remove(7)
print(num2)
print(num1 | num2)
print(num1 & num2)
print(num1-num2)


#stack
books=[]
books.append("Learn C")
books.append("Learn C++")
books.append("Learn Python")
print(books)

books.pop()
print("Now the first book is : ",books[-1])
books.pop()
print("Now the first book is :",books[-1])
books.pop()
if not books:
    print("No books left")


#Queue
from collections import deque
bank = deque(["Tushar","Maruf","Sakib"])
print(bank)
bank.popleft()
print(bank)
if not bank:
    print("No person left")


