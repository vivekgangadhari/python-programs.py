# ##########Task-15,Task-16 ##################
# '''Problem 1 Using 
# break in a While Loop
# Write a Python program that takes a list of numbers as input 
# numbers = [25, 30, 
# 20, 40, 15, 25] and prints the sum of the numbers. However, if the sum exceeds 
# 100, stop adding numbers and print "Sum exceeded 100"'''
numbers=[25,30,20,40,15,45]
sum=0
for i in numbers:
    sum+=i
    if sum>=100:
        break
# print(f"our sum is {sum} and exceeded 100")
# '''Problem 2 
#  Using continue in a For Loop
# Write a Python script that uses a for loop to iterate through numbers from 1 to 
# 600. Print only the odd numbers, skipping the even ones using the continue
# statement'''
for i in range(1,601):
    if i%2==0:
        continue
    else:
        print(i)
# '''Problem 3 
#  Using pass in Conditional Statements
# continue 
# 1
# Write a Python script that checks if a number is even or odd. If the number is 
# even, print "Even"; if odd, do nothing (use the 
# pass statement)'''
number=int(input("enter the number:"))
for i in range(number,number+1):
    if i%2==0:
        print("Even")
    else:
        pass
# '''Problem 4 Combining Transfer Statements
# Write a Python script that iterates through a list of words. If the word is "break," 
# exit the loop using the 
# break statement. If the word is "skip," skip the rest of the 
# code for the current iteration using the 
# continue statement. For any other word, 
# print the word'''
words=["vivek","ramu","uppi","rakesh","skip","break"]  
for item in words:
    if item=="break":
        break
    elif item=="skip":
        continue
    else:
        print(item)
 ###########Task-17 ####################
# Practice using Python List, Indexing,slicing   
#there is concept called indexing in python
#indexing
#syntax
#sequence[index]
list=[6,4,3,2,5,6,7,8,]
print(list[3])
print(list[-1])
print(list[-5])
#slicing
my_list=[7,4,5,6,9,2,3,4]
print(my_list[::-2])
print(my_list[0:4])
print(my_list[1:3:1])
print(my_list[-3:-5:-1])
#nested indexing mainly used in matrix
matrix=[[4,6,7],[7,3,82],[9,5,4]]
print(matrix[1][2])#to access the value 82 
print(matrix[0][1])# for 6
print(matrix[2][1])# for 5
print(matrix[2][0])# for 9



