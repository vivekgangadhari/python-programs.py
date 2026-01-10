####################Task-10 and 11##################################
'''1. Vowel Checker:
Write a Python program that takes a character as input and checks whether
it is a vowel or not. Use the if-else statement.'''
input_alphabet=input("enter the alphabet:")
vowels_charecters="aeiouAEIOU"
if input_alphabet in vowels_charecters:
    print(f"you entered a vowel is:{input_alphabet}")
else:
    print(f"it is not in the list : and you eneterd {input_alphabet}")
'''2. Age Group Classification
Write a program that takes an age as input and classifies the person into
one of the following age groups:
Child: 0-12 years
Teenager: 13-17 years
Adult: 18-64 years
Senior: 65 years and older'''
person_age=int(input("Enetr your Age:"))
if person_age >=65:
    print(f" his age is {person_age} belongs to senior group")
elif person_age >=18:
    print(f" his age is {person_age} belongs to adult group")
elif person_age >=13:
    print(f" his age is {person_age} belongs to Teenager group")
elif person_age>=0:
    print(f" his age is {person_age} belongs to child group")
else:
    print("Invalid credintials please enter the valid age")
'''3. Number Classifier:
Write a program that takes an integer as input and classifies it as positive,
negative, or zero. Use the
if-elif-else statement.'''
input_number=int(input("enter the number:"))
if input_number >0:
    print(f"{input_number} is a positive number")
elif input_number<0:
    print(f"{input_number} is negative number")
else:
    print(f"{input_number} is Zero")
'''4. Leap Year Checker:
Create a program that checks whether a given year is a leap year or not. A
leap year is divisible by 4, but not by 100 unless it is divisible by 400.
'''
year=int(input("enter the year:"))
if year%4==0 or year%400==0:
    print(f"{year} is a leap year")
else:
    print(f"{year} is not a leap year")
''' 5. Calculator:
Build a simple calculator program that takes two numbers and an operator
(+, -, *, /) as input and performs the corresponding operation.
'''
number_1=int(input("enter the number 1:"))
number_2=int(input("enter the number2:"))
operator=input("enter the operator :")
if operator=="+":
    print(f"addition :{number_1+number_2}")
elif operator=="-":
    print(f"subtraction :{number_1-number_2}")
elif operator=="*":
    print(f"multiplication :{number_1*number_2}")
elif operator=="/":
        print(f"division :{number_1/number_2}")
else:
    print("entered wrong operator")

for i in range(1,11):
    for j in range(1,11):    
        print(i,"*",j,"=",i*j)
    print("*"*100)
'''6. Short Hand If:
Rewrite the following code using the short-hand
if statement:
Quiz Questions: 3
x = 8
if x % 2 == 0: result = "Even"
else: result = "Odd"'''
number=9
result="even" if number%2==0  else "odd"
print(result)
'''7. Discount Calculator:
Create a program that calculates the final price after applying a discount.
The program should take the original price and the discount percentage as
input.'''
product_price=int(input("enter the product_price:"))
discount=int(input("enetr the discount:"))
result=(product_price*discount)/100
final=product_price-result
print(f"after applying the dicount of {discount} % to product_price of {product_price} is :{final}")
'''8. BMI Calculator:
Write a program that calculates the Body Mass Index (BMI) using the
formula: BMI = weight (kg) / (height (m))^2. The program should take
weight and height as input.'''
person_weight=float(input("enter the weight(kg):"))
person_height=float(input("enter the height(m):"))
BMI=(person_weight/person_height)**2
print(f"the bmi of person if weight is {person_weight} AND height is {person_height} then BMI is :{BMI}")
'''first we want to take the person_weight as input
then person_height has input from user
calculate the formula(bmi) =(person_weight/person_height)**2
then display the result by calculating of bmi formula we get the out put.'''
