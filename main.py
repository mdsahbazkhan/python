# old_age=input("Please Enter your age  ")

# new_age=int(old_age)+2
# print(new_age)

# float()
# str()
# bool()

# first=input("Enter first number ")
# second=input("Enter second number ")

# sum=int(first)+int(second)
# print("The sum is "+ str(sum))



# name="Tony Stark"

# print(name.find("y"))

# print(name.replace("Tony Stark","Ironman"))
# print(name)


# print("m" in name)

# age=15

# if age >=18:
#     print("You are an adult")
#     print("You can vote")

# elif age<18 and age>3:
#     print("You are in school")

# else:
#     print("You are a child")


# first =input("Enter first number: ")
# operator=input("Enter operator(+,-,/,*,%): ")
# second=input("Enter second number: ")


# if operator=="+":
#     print(int(first)+int(second))
# elif operator=="-":
#     print(int(first)-int(second))
# elif operator=="/":
#     print(int(first)/int(second))
# elif operator=="*":
#     print(int(first)*int(second))
# elif operator=="%":
#     print(int(first)%int(second))
# else:
#     print("Invalid Operation")

# i=1
# while i<=5:
#     print(i*"* ")
#     i=i+1

# List
# marks=[10,11,12,13]

# # marks.append(18)
# marks.insert(2,18)
# # for item in marks:
# #     print(item)
# # print(marks)

# # print(99 in marks)

# print(len(marks))


# marks.clear()

#Tuple
# marks=( 96, 97, 98, 99,95,95)
# print(marks.count(95))
# print(marks.index(95))


#Set
# marks={96, 97, 98, 99, 95, 95}
# print(marks)
# print(marks.pop())
# for mark in marks:
#     print(mark)

#Dictionary
# marks={"english": 95, "chemistry": 98}

# print(marks["chemistry"])
# marks["physics"]=97;
# print(marks)

# Module Function

# from math import *
# import math

# print(dir(math))
# print(sqrt(4))

#User define function

# def sum(a,b=5):
#     return a+b
# print(sum(2, 3))

# JSON ->python

# import json

# data='{"name":"Tony","age":20,"city":"New York"}'

# parse=json.loads(data)
# print(parse)
# print(type(parse))
# print(parse["age"])


# Convert python to JSON

# import json

# data={"name":"Tony","age":20,"city":"New York"}

# json_data=json.dumps(data)
# print(json_data)
# print(type(json_data))

# import requests
# res= requests.get("https://jsonplaceholder.typicode.com/posts")
# data=res.json()
# print("Title----"+data[0]["title"])
# print("Boady---"+data[0]["body"])

# File Handling

# with open("test.txt", "w") as f:
#     f.write("Hello World")

# with open("test.txt","r") as f:
#     content=f.read()
#     print(content)


with open("test.txt","r") as f:
   for line in f:
       print(line.strip()) ##Strip is used to remove leading space and new line

# Error Handling

# Without Error Handling
# x=int(input("Enter First Number: "))
# print(10/x)

# With Error Handling
# try:
#     x=int(input("Enter First Number: "))
#     print(10/x)
# except:
#     print("Error Occured")
    
# try:
#     x=int(input("Enter a number "))
#     print(10/x)
# except ValueError:
#     print("Invalid Number")
# except ZeroDivisionError:
#     print("Cannot divide by zero")

# List Comprehension

# Normal way

# list =[1,2,3,4,5,6]

# square=[]
# for i in list:
#     square.append(i**2)

# print(square)


# List Comprehension way

# list =[1,2,3,4,5,6]
# square=[i**2 for i in list]
# print(square)

# list=[1,2,3,4,5,6]
# even=[i for i in list if i%2==0]
# print(even)


# names=["ali","sahbaz","Umar"]
# upper=[name.upper() for name in names]
# print(upper)

list=[1,2,3,4,5,6]
even_square=[i**2 for i in list if i%2==0]
print(even_square)




