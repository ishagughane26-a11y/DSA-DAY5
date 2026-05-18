#Wipro imp que
# import math

# stack = [79, 77, 54, 81, 48, 34, 25, 16]

# count = 0

# while stack:
#     area = stack.pop()

#     if math.isqrt(area) ** 2 == area:
#         count += 1

# print(count)

# Q.what is the output of the code(MCQ)

# def func(value,values):
#     var=1
#     values[0]=44
# t=3
# v=[1,2,3]
# func(t,v) 
# print(t,v[0])   

#MCQ
# def f(i,values=[]):
#     values.append(i)
#     print(values)
#     #return values
# f(1)  #calling function
# f(2)
# f(3)


##Stack using List
#easy to implement
#speed problem when it grows

#stack using Linked lisy
# Fast performance 
#implementation is not easy


#MCQ
# fruit = {}   #{'Apple':1,'Banana':1,('apple':1}
# def addone(index):
#     if index in fruit:
#         fruit[index] +=1
#     else:
#         fruit[index]=1
# addone('Apple')
# addone('Banana')
# addone('apple')
# print(len(fruit))  
  

#write a program to accept student name and marks from the keyboard and create a dictonary.
# Also display student marks by taking student name.

# n=int(input("Enter the number of students:"))

# d={}

# for i in range(n):
#     name=input("Enter the name of student:")
#     marks=input("Enter the marks:")
#     d[name]=marks   #add key:value

# while True:
#     name=input("Enter students Name to get MArks:")
#     marks=d.get(name,-1) 
#     if marks==-1:
#         print("Student Not Found")
#     else:
#         print("The marks of",name,"are",marks)

#         option=input("Do you want to find another Student marks[Yes/No]")
#         if option=="No":
#             break
# print("Thanks for using our Apllication")    

# write a program to acces each charecter of string in forward and backward direction by using 
# while loop?         I/P="learning python is very easy"


# s="learning python is very easy"
# i=0
# print("Forward direction")

# while i < len(s):
#     print(s[i],end="")
#     i+=1

# i = len(s) - 1
# print("\nBackward Direction:")

# while i >= 0:
#     print(s[i], end="")
#     i -= 1

#Example
#Input strings
# data = "abcdfjgerj abcdfijger"


# for i in range(len(data)):
    
#     # Check for space
#     if data[i] == " ":
        
#         # Print previous character
#         print(data[i-1])

#
# v=['a','e','i','o','u']
# w=input("Enter the word where we will search the vowels:")
# found=[]
# for i in w:
#     if i in v:
#         if i not in found:
#             found.append(i)
# print('Found vowels=',found)
# print('Unique vowels',len(found),'from the given word=',w)            


#
# x,y,z =map(int,input().split())
# mylist=[] #29 38 12 48 39 55
# for i in range(x):
#     a=int(input())
#     mylist.append(a)
    
# for j in mylist:
#     if j>=y and j<=z:
#         print(j,end='')


#
# import datetime
# #datetime formatting
# date=datetime.datetime.now()
# print("It's now:{:%d/ %m /%y  %H:%M:%S}".format(date))

# x=['A','B','C']
# y=['A','B','C']
# z=[1,2,3,4]
# print(x==y)
# print(x==z)
# print(x!=z)

# List comhresion
# s=[1,4,9,16,25,36,49,64,81,100]
# val=[2**i for i in range(1,6)]
# print(val)

# val2=[i for i in s if i%2==0]
# print(val2)

# s=[i*i for i in range(1,11)]  #i=4
# print(s)

#Dictonary comphression:
# squares={x:x*x for x in range(1,6)}
# print(squares)

# doubles={x:2*x for x in range(1,6)}
# print(doubles)

#multile vales in single line

# a,b=[int(x) for x in input("Enter 2 numbers :").split()]
# print("Product is:",a*b)

# a,b,c= [float(x) for x in input("Enter 3 float numbers:").split(',')]
# print("The sum is :",a+b+c)


#using else block
# mycart=[10,20,800,500,400,60,70]
# for item in mycart:
#     if item>400:
#         print("This is not in my budget")
#         continue
#     print(item)
# else:
#     print("you have purchessd evrything")

# username="admin"
# passward="admin"
# Enter username
# Enter passward

# while True:
#    username=input("Enter username:")
#    passward=input("Enter passward:")
#    if username=='admin' and passward=='admin':
#       print("login Successfully")
#       break
#    else:
#       print("Invalid")


  
#Tower of Hanoi
import time

class Tower:

    def __init__(self):
        print("Welcome To Tower of Hanoi Game")
        print()
        print("Given problem  A=[3,2,1]   B=[]   C=[]")
        print()
        print("Expected output  A=[]   B=[]   C=[3,2,1]")

        self.A = []
        self.B = []
        self.C = []

    def tower(self, item):
        self.A.append(item)
        time.sleep(1)
        print("A =", self.A)
        print("Items in Tower A\n")

    def pass1(self):
        self.temp = self.A.pop()
        self.C.append(self.temp)
        time.sleep(1)
        print("A=", self.A, "   B=", self.B, "   C=", self.C)
        print("Pass One Completed====================\n")

    def pass2(self):
        self.temp = self.A.pop()
        self.B.append(self.temp)
        time.sleep(1)
        print("A=", self.A, "   B=", self.B, "   C=", self.C)
        print("Pass Two Completed====================\n")

    def pass3(self):
        self.temp = self.C.pop()
        self.B.append(self.temp)
        time.sleep(1)
        print("A=", self.A, "   B=", self.B, "   C=", self.C)
        print("Pass Three Completed====================\n")

    def pass4(self):
        self.temp = self.A.pop()
        self.C.append(self.temp)
        time.sleep(1)
        print("A=", self.A, "   B=", self.B, "   C=", self.C)
        print("Pass Four Completed====================\n")

    def pass5(self):
        self.temp = self.B.pop()
        self.A.append(self.temp)
        time.sleep(1)
        print("A=", self.A, "   B=", self.B, "   C=", self.C)
        print("Pass Five Completed====================\n")

    def pass6(self):
        self.temp = self.B.pop()
        self.C.append(self.temp)
        time.sleep(1)
        print("A=", self.A, "   B=", self.B, "   C=", self.C)
        print("Pass Six Completed====================\n")

    def pass7(self):
        self.temp = self.A.pop()
        self.C.append(self.temp)
        time.sleep(1)
        print("A=", self.A, "   B=", self.B, "   C=", self.C)
        print("Pass Seven Completed====================\n")


obj = Tower()

obj.tower(3)
obj.tower(2)
obj.tower(1)

obj.pass1()
obj.pass2()
obj.pass3()
obj.pass4()
obj.pass5()
obj.pass6()
obj.pass7()


