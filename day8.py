###############Task -18 and Task-19 ##############################
'''Task 1:
Reverse List:
Write Python code to reverse the order of elements in the given list my_list .
Print the reversed list.
my_list = [10, 20, 30, 40, 50, 11]
# Your code here
# Output should be: [11,50,40,30,20,10]
'''
# 1st method
my_list=[10,20,30,40,50,11]
print(my_list[::-1])
#2nd method
my_list=[10,20,30,40,50,11]
my_list.reverse()
print(my_list)
#3rd method
my_list=[10,20,30,40,50,11]
reverse=[]
for i in my_list:
    reverse.insert(0,i)
print(reverse)
'''Task 2:
Common Elements:
Given two lists list1 and list2 , find and print the common elements between
them.
list1 = [1, 2, 3, 4, 5]
list2 = [4, 5, 6, 7, 8]
# Your code here
# Output should be: [4, 5]
'''
my_list=[]
my_list1=[1,2,3,4,5]
my_list2=[4,5,6,7,8]
for i in my_list1:
    for j in my_list2:
        if i==j:
            my_list.extend([i])
print(my_list)
'''Task 3:
Unique Elements:
Create a new list unique_list containing only the unique elements from the
given list original_list . Print the unique list.
original_list = [1, 2, 2, 3, 4, 4, 5]
# Your code here
# Output should be: [1, 2, 3, 4, 5]
'''
unique_list=[]
original_list=[1,1,1,1,2,3,4,5,2,3,4,4,5,5]
for item in original_list:
    if item not in unique_list:
        unique_list.append(item)
print(unique_list)
'''Task 4:
Remove Duplicates:
Remove duplicate elements from the given list duplicated_list and print the list
without duplicates while preserving the order.
duplicated_list = [1, 2, 2, 3, 4, 4, 5]
# Your code here
# Output should be: [1, 2, 3, 4, 5]'''
duplicated_list=[]
duplicate_list=[1,1,1,1,1,3,4,6,7,7,7,7,2,2,3,4,4,5]
for i in duplicate_list:
    if i not in duplicated_list:
        duplicated_list.append(i)
duplicate_list.clear()
duplicate_list.extend(duplicated_list)
print(duplicate_list)
'''Exercise 1: List Concatenation
Write a Python script that concatenates two lists and prints the result.'''
my_list1=[1,2,3,4,7]
my_list2=[9,5,2,7,0]
my_list1.extend(my_list2)
print(my_list1)
'''Exercise 2: List Repetition
Write a Python script that repeats a list three times and prints the result.
'''
my_list=[1,3,5,"vivek",7]
for i in range(0,3):
    print(my_list)
my_list=[1,2,3,4]
repeated=my_list*3
print(repeated)
'''Exercise 3: List Removal
Write a Python script that removes the elements at even indices from a list'''
my_list=[1,2,3,4,5,6,7,8,9,10]
result=my_list[1::2]
print(result)
'''Exercise 4: List Insertion
Write a Python script that inserts the numbers 10, 11, and 12 at the beginning of
a list
'''
old_baskets=[1,2,3,4,5,6]
basket_numbers=[10,11,12]
result=basket_numbers+old_baskets
print(result)
#using insert() logic
my_list=[1,2,4,5,6]
my_list.insert(0,10)
my_list.insert(0,11)
my_list.insert(0,12)
print(my_list)
'''List comprehensions
1. Square Numbers: Create a list of squares of numbers from 1 to 10.
2. Even Numbers: Generate a list of even numbers from 1 to 20.
3. Words Lengths: Given a list of words, create a list containing the lengths of
each word.
words = ["apple", "banana", "cherry", "date"]'''

#1. Square Numbers: Create a list of squares of numbers from 1 to 10.
#general method 1
squares=[]
for i in range(1,11):
    result=i**2
    squares.append(result)
print(squares)
#method 2
result=[x**2 for x in range(1,11)]
print(result)
# #method 3
print([i**2 for i in range(1,11)])
#2. Even Numbers: Generate a list of even numbers from 1 to 20.
# #method 1
even_numbers=[]
for i in range(1,21):
    if i%2==0:
        even_numbers.append(i)
print(even_numbers)
#method2
result=[x for x in range(1,21) if x %2==0]
print(result)
# #method 3
print([x for x in range(1,21) if x%2==0])
'''3. Words Lengths: Given a list of words, create a list containing the lengths of
each word.
# words = ["apple", "banana", "cherry", "date"]'''
#method1
words = ["apple", "banana", "cherry", "date"]
words_length=[]
for i in words:
    words_length.append(len(i))
print(words_length)
#method 2
words = ["apple", "banana", "cherry", "date"]
print([len(i) for i in words ])
#method 3
print([len(i) for i in ["apple", "banana", "cherry", "date"] ])
# List comprehensions:
'''these are used to write the list concept in easy
and in less space and make the program concise'''
 
    
  



    

