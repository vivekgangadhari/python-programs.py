'''Dictionary of words
Create a program that manages a dictionary of word meanings. The program
should allow users to perform the following actions:
1. Add a Word: Allow users to add new words along with their meanings to the
dictionary.
2. Search for Meaning: Enable users to search for the meaning of a word in the
dictionary.
3. Display All Words: Provide an option to display all words and their meanings
currently stored in the dictionary.
4. Update Meaning: Implement a feature to update the meaning of an existing
word in the dictionary. After updating, display the updated meaning.
5. Delete Word: Implement a feature to delete a word and its meaning from the
dictionary. Confirm the deletion and handle cases where the word doesn't
exist.
6.exit the program
7.shows number of words in the dictionary
8.checks dictionary is empty or not
Ensure the program handles invalid inputs gracefully. Use a while loop to keep the
program running until the user chooses to exit.'''
############################ Task-23 #############################
########################## Mini Project ############################
dictionary={}
while True:
    print("\n Dictionary Management System")
    print("1. Add a word to dictionary")
    print("2. Search for Meaning")
    print("3. Display All Words")
    print("4. Update Meaning")
    print("5. Delete Word")
    print("6. shows the number of words in the dictionary")
    print("7.checks dictionary is empty or not")
    print("8.exit the program")

    user_choice=input("enter the choice :")
    # first choice
    if user_choice=="1":
        word=input("enter the word to add :").upper()
        meaning=input("enter the meaning to add :").lower()
        dictionary[word]=meaning
        print(f" word and meaning addedd succeessfully in dictionary")
        #second choice
    elif user_choice=="2":
        user_word=input("enter the word  to search :").upper()
        if user_word in dictionary:
            print("meaning :",dictionary[user_word])
        else:
            print(f"word not found in the dictionary")
            #third choice
    elif user_choice=="3":
        if dictionary:
            print("words and meanings")
            for i,j in dictionary.items():
                print(f"{i}:{j}")
        else:
            print("empty dictionary,dictionary do not contain anything please add words to dictionary to display.")
    elif user_choice=="4":
        user_word=input("enter the word to which we want to add the new  meaning:").upper()
        if user_word in dictionary:
            new_meaning=input("enter the meaning :").lower()
            dictionary[user_word]=new_meaning
            print(f'''{user_word}:{dictionary[user_word]}," :this is the updated meaning''')
            print("new_meaning of word addedd successfully")
        else:
            print("word not in dictinory")
    elif user_choice=="5":
        user_word=input("enter the word:").upper()
        if user_word in dictionary:
            del dictionary[user_word]
            print(f"removed {user_word} successfully from dictionary")
        else:
            print("the word not have in the dictionary")
    elif user_choice=="6":
        print("The number of words in dictionary are :",len(dictionary))
    elif user_choice=="7":
        if dictionary:
            print("dictionary is not empty")
        else:
            print("dictionary is empty")
    elif user_choice=="8":
        print("thank you for using the Dictionary \U0001F600 ")
        break
    else:
        print("invalid choice, please enter the correct choice")
