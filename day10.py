#########################Task-24 ##############################
'''Task 1: Set Intersection
Write Python code to find and print the intersection of the following two sets:
set1 = {1, 2, 3, 4, 5}
set2 = {4, 5, 6, 7, 8}
# Your code here
# Output should be: {4, 5}'''
set1 = {1, 2, 3, 4, 5}
set2 = {4, 5, 6, 7, 8}
set3=set1.intersection(set2)
print(set3)
'''Task 2: Set Union
Write Python code to find and print the union of the following two sets:
set1 = {1, 2, 3, 4, 5}
set2 = {4, 5, 6, 7, 8}
# Your code here
# Output should be: {1, 2, 3, 4, 5, 6, 7, 8}'''
set_1={1,2,3,4,5}
set_2={4,5,6,7,8}
set_3=set_1.union(set_2)
print(set_3)
'''Task 3: Set Difference
set2 :
Write Python code to find and print the elements present in 
set1 = {1, 2, 3, 4, 5}
set2 = {4, 5, 6, 7, 8}
set1 but not in 
2
# Your code here
# Output should be: {1, 2, 3}
'''
set_1={1,2,3,4,5}
set_2={4,5,6,7,8}
set_3=set_1.difference(set_2)
print(set_3)
'''Task 4: Set Symmetric Difference
Write Python code to find and print the symmetric difference of the following 
two sets:
set1 = {1, 2, 3, 4, 5}
set2 = {4, 5, 6, 7, 8}
# Your code here
# Output should be: {1, 2, 3, 6, 7, 8}'''
set1={1,2,3,4,5}
set2={4,5,6,7,8}
set3=set1.symmetric_difference(set2)
print(set3)
'''Task 5: Set Membership Test
Write Python code to check if the element 3 is present in the set 
my_set = {1, 2, 3, 4, 5}
# Your code here
# Output should be: True
'''
my_set={1,2,3,4,5}
print(3 in (my_set))
'''Exercise 1: Set Intersection
my_set :
Write a Python script that finds and prints the intersection of two sets.'''
set1={11,9,6,4,3}
set2={8,4,5,9,3}
set3=set1.intersection(set2)
print(set3)
'''Exercise 2: Set Union
Write a Python script that finds and prints the union of two sets'''
set1={3,6,5,3,2,8}
set2={8,3,5,9,2,5}
print(set1.union(set2))
'''Exercise 3: Set Difference
Write a Python script that finds and prints the difference between two sets'''
set1={3,4,5,9,8}
set2={6,7,9,2,1,5}
print(set1.difference(set2))
'''Exercise 4: Set Symmetric Difference
Write a Python script that finds and prints the symmetric difference between 
two sets.'''
set1={1,2,3,4,5}
set2={5,4,7,8,9}
print(set1.symmetric_difference(set2))
################## Task-25 ##################
'''Coding Exercise:
1)Create a Tuple: Write a program that creates a tuple containing three 
elements: your name, your age, and your favorite color. Then print the tuple '''
my_tuple=("Vivek",21,"green")
print(my_tuple)
'''2)Access Tuple Elements Write a program that creates a tuple containing the 
days of the week. Then, print the third element of the tuple'''
days_names=("monday","tuesday","wednesday","thursday","friday","saturday","sunday")
print(days_names[2])
'''3) Tuple Concatenation Write a program that creates two tuples, one 
containing odd numbers from 1 to 5 and another containing even numbers 
from 2 to 6. Concatenate these two tuples and print the result'''
tuple_1=(1,3,5)
tuple_2=(2,4,6)
result=tuple_1+tuple_2
print(result)
'''4) Tuple Unpacking Write a program that defines a tuple containing the 
dimensions of a rectangle (length and width). Then, unpack this tuple into 
two variables and calculate the area of the rectangle'''
#method 1
tuple_1=(20,30)
length=tuple_1[0]
breadth=tuple_1[1]
print(f" Area of Rectangle Is :{length*breadth}") 
#method 2 unpacking
len,bre=tuple_1
print(f"area of rectangle is :{len*bre}")
'''5)Check if an Element Exists Write a program that checks if a given element 
exists in a tuple.'''
friends_names=("aravind","vignesh","shiva","upender","abhilash","srikar")
print("vignesh" in friends_names)
'''6)Write a Python program to generate a bill for a supermarket purchase. The 
program should store the items and their prices in a list of tuples. It should 
then iterate over this list to print out each item along with its price. Finally, 
calculate and print the total cost of all the items'''
#sample input and output
products=[('sugar',45),('oil',120),('chakra gold',10),('santoor soap',20)]
print("items\t\tprice")
print("_"*30)
sum=0
for items,prices in products:
    print(f"{items:<20}{prices}")
    sum+=prices
print("_"*30)
# price_width=20
# item_width=20
# print(f"{'total':<{item_width}}{sum:>{price_width}}")
print(f"total\t\t\t{sum}")
print("_"*30)
#i can do this work later 
'''#sample input and output
products=[('sugar',45),('oil',120),('chakra gold',10),('santoor soap',20)]
print("items\t\tprice")
print("_"*30)
sum=0
for items,prices in products:
    print(f"{items:<20}{prices}")
    sum+=prices
print("_"*30)
# price_width=20
# item_width=20
# print(f"{'total':<{item_width}}{sum:>{price_width}}")
print(f"total\t\t\t{sum}")
print("_"*30)
'''
