#Q1) Age group Categorizations

# Age=int(input("Please enter the age: "))

# if Age<13:
#     print("child")
    
# elif Age<20:
#     print("Teenager")
    
# elif Age<60:
#     print("Adult")
    
# else:
#     print("Senior")




# Q2) Movie Ticket with discount 

# age= int(input("Enter your age: "))

# day=input("Enter the day: ")

# price=0

# if age>=18:
#     price=12
    
# else:
#     price=8

# if day =="Wednesday":
#     price=price-2
    
# print(price,"$")


# Q3) Grade calculator


Marks=int(input("Please enter your marks: "))

if Marks >= 101:
    print("Please Try Again!")
    exit()

if Marks>=90:
    print("Grade: A")
    
elif Marks>=80:
    print("Grade: B")
    
elif Marks>=70:
    print("Grade: C")
    
elif Marks>=60:
    print("Grade: D")
    
else:
    print("Grade: F")