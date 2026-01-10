################Task-12########################
#observation about the stack overflow website

'''stack overflow is a website used to post the programming questions where
lot of people can use this to improve the knowledge so sir as you said
i have visted the official website and i have created the stack overflow 
profile and i posted one question about nested for loop  in stack overflow.'''
##############Task-13 and Task-14###############################
'''Exercise 1: Sum of Squares
Write a Python program that calculates and prints the sum of the squares of
numbers from 1 to 5 using a
for loop.'''
sum=0
for item in range(1,6):
    square=item**2
    sum+=square
print(sum)
'''Exercise 2: Countdown
Write a Python program that uses a
while loop to print a countdown from 5 to 1.'''
num=5
while num>=1:
    print(num)
    num -=1

'''Exercise 3: Multiplication Table with Nested For Loop
Write a Python program to print the multiplication table for a user-specified
number using a nested for loop.'''
table_number=int(input("enter the table:"))
for i in range (table_number,table_number+1):
    for j in range(1,11):
        print(f" {i} x {j}={i*j}")
'''Exercise 4:
Write a Python program that uses a "for" loop to find the sum of all even
numbers between 0 and 10 (inclusive).
'''
sum=0
for i in range(0,11):
    if i%2==0:
        sum+=i
print(sum)
'''Exercise 5:
Calculate the sum of all numbers from 1 to a given number'''
user_number=int(input("enetr the number:"))
sum=0
for i in range(1,user_number+1):
    sum +=i
print(f"the sum of given numbers is :{sum}")
''' Exercise 6:
Display numbers from a list using loop
'''
fruits=["banana","apple","orange","pineapple","mango","grapes"]
for items in fruits:
    print(items)
numbers=[1,4,7,9,45,3,32]
for items in numbers:
    print(items)
'''Exercise 7:
Display numbers from -10 to -1 using for loop'''
for item in range(-10,0):
    print(item)
'''Exercise 8:
Write a Python program to print the cube of all numbers from 1 to a given
number
'''
user_number=int(input("enter the number:"))
for i in range(1,user_number+1):
    cube=i**3
    print(f"the cube of {i} is :{cube}")


