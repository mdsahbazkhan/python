# Count Positive number

numbers=[1,-2,3,-4,5,6,-7,-8,9,10]

count=0
for num in numbers:
    if num >0:
        count+=1

# print(count)


# Sum of Even Number
# N=20

sum_of_even=0

# for i in range(1,N+1):
#     if i%2 ==0:
#         sum_of_even+=i
        
# print(sum_of_even)


# number=3

# for i in range(1,11):
#     if i != 5:
#         print(number ,'X', i, '=', number*i)


# Reverse String

# str="Python"

# reverse=""

# for char in str:
#     reverse=char+reverse
    
# print(reverse)

# Factorial

# num=6
# fact=1
# while num>0:
#     fact*=num
#     num-=1
    
# print(fact)


# Prime number
# num=9
# is_Prime=True

# if num>1:
#     for i in range(2,num):
#         if (num % i)==0:
#             is_Prime=False
#             break
 
# else:
#     is_Prime=False           

# print(is_Prime)  

# List Uniquenes Checker

# items=["apple","orange","banana","apple","mango"]   

# unique_item=set()

# for item in items:
#     if item in unique_item:
#         print("Duplicate: ", item)
#         break
#     unique_item.add(item)



# Wait tiem every attempt multiply wait time by 2 and max attempt will be 5

import time

wait_time=1
attempt=0
max_attempt=5

while attempt<max_attempt:
    print("Attempt", attempt+1 , "-wait time", wait_time)
    time.sleep(wait_time)
    wait_time*=2
    attempt+=1
    
    
    
    