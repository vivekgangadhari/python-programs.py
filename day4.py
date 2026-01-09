#######################Task 8######################
'''Write a Python program to calculate the area of a rectangle using the given
formula: area = length * width . Take the values of length and width as inputs from
the user.'''
#calculating area of a rectangle
length=int(input("enetr the length:"))
width=int(input("enter the width:"))
area=length*width
print(f"area of a rectangle is : {area}")
#Write a Python program to demonstrate incrementing and decrementing a variable
num_1=int(input("enter the number1:"))
num_2=int(input("enter the number2:"))
# #incrementing the value by 5
num_1 +=5
print(num_1)
#decerementiong the value by 4
num_2 -=4
print(num_2)
'''Write a Python program to convert temperature from Celsius to Fahrenheit. The
formula for conversion is: F = (C * 9/5) + 32 . Take the temperature in Celsius as input from the user.'''
c=int(input("enter the celcius:"))
foren_heat=(c*9/5)+32
print(foren_heat)
#simple intrest calculation in python
principal_amount=float(input("enter the amount"))
time_period=float(input("enter the time:"))
rate_ofinterest=float(input("enter the percentage:"))
result=(principal_amount*time_period*rate_ofinterest)/100
principal_amount -= result
print(f"after 1 year the intrest came is{result} and final principal amount is {principal_amount}")
'''Write a Python program to concatenate two strings and display the result. The
strings should be taken as input from the user.'''
first_name=input("enter the name1:")
last_name=input("enter the last name:")
result=first_name+last_name
print(result)
#Write a Python program to convert a distance from kilometers to miles
kilometers=float(input("enetr the number of kilometers:"))
miles=kilometers*0.621371
print(f"{kilometers} Kilometers is equal to :{miles} miles")
#################Task 9##################
'''Exercise: Create a program that takes user input for their name and age.
Use formatted strings (f-strings) to print a message welcoming the user and
stating their age.'''
user_name=input("enter the name:")
user_age=int(input("enetr the age:"))
print(f"welcome to  the Gunnies world record competition  Mr.{user_name} Garu at the age of {user_age} years")
''' Create a list called numbers that contains integers from 1 to 10.
Check if the number 5 is in the list.
Check if the number 15 is not in the list.'''
my_list=[1,2,3,4,5,6,7,8,9,10]
first_num=5
second_num=15
print(first_num  in my_list)
print(second_num not in my_list)








