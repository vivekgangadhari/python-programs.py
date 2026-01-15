########################### Task-20 ###########################
'''Coding Exercise :
Problem:
You are given a string sentence . Print the characters at even indices.
Example:
sentence = "Python is amazing"
# Output: "Pto saaig"'''
new_sentence=''''''
sentence="Python is amazing"
print(sentence[::2])
print(type(sentence))
#out put:  Pto saaig
'''Problem:
You are given a string s . Replace all spaces in the string with underscores ( _ )
and print the modified string.
Example:
s = "Python is fun and powerful"
# Output: "Python_is_fun_and_powerful"'''
s = "Python is fun and powerful"
print(s.replace(" ","_"))
'''Problem:
You are given a string s . Check if the string contains only digits.
Example:'''
s = "12345"
checking_s=s.isdigit()
print(checking_s)
'''Problem:
You are given a string s . Print the string in reverse order.
Example:
s = "Python is amazing"
# Output: "gnizama si nohtyP'''
s = "Python is amazing"
reverse=s[::-1]
print(reverse)
'''Problem:
You are given a string s . Capitalize the first letter of each word in the string
and print the modified string.
Example:
s = "python programming is fun"
# Output: "Python Programming Is Fun"'''
s = "python programming is fun"
lower=s.lower()
upper=s.upper()
capital=s.title()
print(capital)
########################### Task-21 And Task-22 #############################
'''Task 1: Dictionary Update
Write Python code to add a new key-value pair to the following dictionary:
my_dict = {'name': 'python', 'age': 25}
# Your code here
# Output should be: {'name': 'python', 'age': 25, 'city': 'we
st godavari'}
'''
#method 1
my_dict={'name': 'python', 'age': '25',}
my_dict.update({'city':'west godavari','state':'andhra pradesh',})
print(my_dict)
# method 2
my_dict={'name': 'python', 'age': '25',}
my_dict["city"]="hyderabad"
my_dict["state"]="telangana"
print(my_dict)
'''Task 2: Dictionary Access
Write Python code to access and print the value associated with the key 'price' in
the following dictionary:
product_info = {'name': 'Laptop', 'brand': 'Dell', 'price': 1
200}
# Your code here
# Output should be: 1200
'''
product_info = {'name': 'Laptop', 'brand': 'Dell', 'price': 1200}
value=product_info.get('price')
print(f"value of price is:{value}")
'''Task 3: Dictionary Removal
Write Python code to remove the key-value pair with the key 'city' from the
following dictionary:
my_dict = {'name': 'python', 'age': 30, 'city': 'Bhimavaram'}
# Your code here
# Output should be: {'name': 'John', 'age': 30}'''
my_dict = {'name': 'python', 'age': 30, 'city': 'Bhimavaram'}
new_dict=my_dict.pop('city')
print(my_dict)
'''Task 4: Dictionary Keys
Write Python code to print all the keys present in the following dictionary:
my_dict = {'name': 'python', 'age': 25, 'city': 'Rajahmundr
y'}
# Your code here
# Output should be: ['name', 'age', 'city']'''
my_dict = {'name': 'python', 'age': 25, 'city': 'Rajahmundry'}
print(my_dict.keys())
'''Task 5: Dictionary Values
Write Python code to print all the values present in the following dictionary:
my_dict = {'name': 'python', 'age': 25, 'city': 'tanuku'}
# Your code here
# Output should be: ['python', 25, 'tanuku']
'''
my_dict = {'name': 'python', 'age': 25, 'city': 'tanuku'}
print(my_dict.values())
print(my_dict.items())
'''Exercise 1: Dictionary Update
Write a Python script that updates a dictionary with a new key-value pair.
'''
#method1 adding new key value pair
basket={"apple":120,"banana":50,"orange":130}
basket.update({"water mealon":70,"pine apple":80})
print(basket)
# method 2 replacing old value(changed the value of apples from 120 to 100)
basket={"apple":120,"banana":50,"orange":130}
basket.update({"apple":100})
print(basket)
'''Exercise 2: Dictionary Access
Write a Python script that accesses and prints the value associated with a specific
key in a dictionary.'''
dict={1:"car",2:"bike",3:"auto",4:"bus",5:"train"}
value=dict.get(2)
print(f"for the key the value is:{value}")
'''Exercise 3: Dictionary Removal
Write a Python script that removes a key-value pair from a dictionary.'''
my_dict={'car':120000,"bike":100000,"auto":200000}
my_dict.pop('bike')
print(my_dict)
'''Exercise 4: Dictionary Keys
Write a Python script that prints all the keys present in a dictionary.
'''
subjects_books={'cns':"rakesh",'cd':'vijay raj','cc':'rajesh','sppm':'anusha','swm':'laxmi',}
print(subjects_books.keys())
'''Exercise 5: Dictionary Values
Write a Python script that prints all the values present in a dictionary.'''
subjects_books={'cns':"rakesh",'cd':'vijay raj','cc':'rajesh','sppm':'anusha','swm':'laxmi',}
print(subjects_books.values())





