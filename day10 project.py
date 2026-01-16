###############Task 26#######################
#Project Super market bill generation
'''Build a Python-based supermarket billing system that allows users to view a list of products, add items to their cart, calculate the total bill with tax, and display a receipt.
Functional Requirements:

    User Interaction:
        The system should ask for the customer’s name.
        Display a list of available products with their prices.
        Allow users to add multiple items to their cart.
        Validate that the quantity entered is a valid number.
        Display an itemized bill with total and tax before exiting.

    Product Catalog:
        Maintain a dictionary of products and their prices.
        Display the product list when requested.

    Billing and Calculations:
        Compute the total price based on item quantities.
        Apply a 12% tax on the total amount.
        Display a detailed invoice with:
            Item name
            Quantity
            Price per unit
            Total price for each item
            Total amount before and after tax

    Receipt Format:
        Display a well-formatted bill with store name, location, and transaction details.

    Exit Mechanism:
        Allow users to exit the purchase process at any time.
        Display a "Thank you" message upon exiting.'''
#practice
# while True:
#     products=[('sugar',45),('oil',120),('chakra gold',10),('santoor soap',20)]
#     for items,price in products:
#         print(f"{items}{price}")
#     print("press 1 to shop and press 2 to exit")
#     choice=input("enter the choice:")
#     if choice=="1":
#         user_name=input("enter your name :")
    



# products=[('sugar',45),('oil',120),('chakra gold',10),('santoor soap',20)]
# print("items\t\tprice")
# print("_"*30)
# sum=0
# for items,prices in products:
#     print(f"{items:<20}{prices}")
#     sum+=prices
# print("_"*30)
# # price_width=20
# # item_width=20
# # print(f"{'total':<{item_width}}{sum:>{price_width}}")
# print(f"total\t\t\t{sum}")
# print("_"*30)
# print("*"*20,"Maha Dev Supermarket","*"*20)
# print(" "*25,"Ghatkesar")
# while True:
#     print()
#correct code#
user_name=input("enter your name:")
products={
    "milk":20,
    "chips":30,
    "oil":120,
    "soaps":30,
    "colgate":20,
    "choclate":20,

}
cart={}
while True:
    print("\n Available products are:")
    print("items\t\t price")
    for items,prices in products.items():
        print(f"{items:<20}{prices}")
    
    print("press 1 to add item")
    print(" press 2 to exit and get bill")
    choice=input("enter the choice :")
    if choice=="1":
        item_name=input("enter the item_name :").lower()
        if item_name in products:
            quantity=int(input("enter the quantity :"))
            cart[item_name]=cart.get(item_name,0)+quantity
        else:
            print(f"{item_name} item out of stock")
    elif choice=="2":
        print("Thank you")
        break
    else:
        print("invalid choice")
print("=========================Maha Dev Supermarket=============================")
print("                               Ghatkesar                           ")

import datetime
now=datetime.datetime.now()
date=now.strftime("%d-%m-%Y")
time=now.strftime("%H:%M")
print("Date :",date)
print("Time:",time)
print(f"Customer Name:{user_name}")
print(75*"-")
print("sno\t\titem\t\tquantity\t\tprice")
total_amount=0
sno=1
for item,quantity in cart.items():
    rate=products[item]
    price=quantity*rate
    total_amount+=price
    tax_amount=(total_amount*12)/100
    final_amount=total_amount+tax_amount
    print(f"{sno}\t\t{item}\t\t{quantity}\t\t\t{price}")
    sno+=1
print(75*"-")
print(50 * " ",'tOtal amount ' 'Rs :',total_amount)
print("tax amount",50*" ",'Rs :',tax_amount)
print(75*"-")
print(50*" ",'Final amount','Rs :',final_amount)
print(75*"-")
print(20*"-","Thank you for shopping &visit again \U0001F600 ",10*"-")
print("-"*75)