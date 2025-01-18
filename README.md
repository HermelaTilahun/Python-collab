# Python-collab
## Python-project-collab
#1) Create a simple Python program application that does the following:

    # Prints "Hello User!"

    # Then asks "What is your name?"

    # Then responds "Hello <user's name>"

    # Then asks: "What is your year of birth?"

    # Then ask: "Do you know how to drive?"

    # Then ask: "How old were you when you got your driving license" if the user replied "Yes" to the above question

    # Then outputs: "You got your driving license in <year> and you have been driving for <x> years" 

    # Then outputs: "You are <age> years old now but you still can't drive. You were supposed to get your license in <year>,<x> years ago at the age of 30 at the latest" If the user replied "No" and is over the age of 30

    # Then outputs: "You are <age> years old now and you should work on getting your driving license before you turn 30. You have <x> years to go until the year <year>" If the user replied "No" and is under the age of 30
    

###-------------------//-------------------------------
#2) Number Chain
    # In this activity, you will take user input and print out a series of numbers.

    # Instructions
    # Using a while loop, ask the user "How many numbers?", and then print out a chain of numbers in increasing order, from 0 to the user-input number.

    # After the results have been printed, ask the user if they would like to continue .

    # If "y" is entered, keep the chain running by inputting a new number and starting a new count from 0 to the new user-input number.

    # If "n" is entered, exit the application.

    # Bonus
    # Rather than just displaying numbers starting from 0, have the numbers begin at the end of the previous chain.

###-------------------//-------------------------------
##3) Manipulating lists 
        # You may be familiar with adding individual data elements to a list by using the .append() method. However, if you want to combine a list with another array type(list, set, tuple), you can use the .extend() method on the list.

        # You can also use the .index() method to find the position of an item in a list. You can then use that position to remove the item with the .pop() method.

        # In this exercise, you'll practice using all these methods!

        # Ask 4 students at Datanomics to enter their names one at a time
        
        # Add their names to the list

student_names = ['Muluken', 'Bethelhem', 'Samuel', 'Workneh']

        # Extend the list student_names using the .extend() list method with two additional new students 


        # Print student_names


        # Find the position of one of the students and store the result in a variable called 'position'
       
position = 2

        # Remove that student  from the list student_names using the .pop() list method
       

        # Print student_names one more time

print(student_names)

###-------------------//----------------------------------------

## 4) Looping over lists
        # You can use a for loop to iterate through all the items in a list. You can take that a step further with 
        # the sorted() function which will sort the data in a list from lowest to highest in the case of numbers and alphabetical order if the list contains strings. 

        # The sorted() function returns a new list and does not affect the list you passed into the function. You can learn more about sorted() in the Python documentation.

        # A list of lists, records has been pre-loaded. If you explore it in the IPython Shell, you'll see that each entry is a list of this form:

        # ['2011', 'FEMALE', 'Ethiopia', 'Abigail', '13', '75']

        # The name of the student 'Abigail' for example is the fourth entry of the third list in the list of lists 'records'. Your job in this question is to loop over this list of lists and append the names of each student to 'student_names' list.


        ## USE the same list: student_names and loop over another list called records

        # Add the name to the list
        # Sort the names in alphabetical order
        # Print each name

records = [['2014', 'FEMALE', 'USA', 'Bethelhem', '10', '40'], ['2014', 'FEMALE', 'USA', 'Workaferahu', '27', '23'], ['2014', 'FEMALE', 'USA', 'Nardos', '31', '19'], ['2014', 'MALE','USA', 'Abel', '10', '40'], ['2014', 'MALE', 'USA', 'Abiy', '27', '23'], ['2014', 'MALE', 'USA', 'Lemessa', '31', '19'], ['2011', 'FEMALE', 'Ethiopia', 'GENET', '13', '75'], ['2014', 'MALE', 'ETHIOPIA', 'Abebe', '10', '40']]

###-------------------//-------------------------------
#5) Write a python program for a simple bank that accepts deposits, processes withdrawals and gives simple interest on deposits
        # your program should ask if the user wants to deposit or withdraw money
        # the program should perform the operation based on the user's response
        # then, the user should be notified of the activity and the final balance once the activity has taken place. 
        # the program should also calculate the simple interest and the original principal from the current balance, assuming that the user's final balance has been 
# in the user's account for 5 years now and a 4% rate of interest.
        # Finally, the program should let the user know how much balance he/she currently has, how long it's been saved, and how much of the balance is accrued interest.

###-------------------//-------------------------------
#6) In this activity, you will create the code that a candy store will use in their state-of-the-art candy vending machine.

        # Instructions
        # Create a loop that prints all of the candies in the store to the terminal, with their index stored in brackets beside them.

        # For example: "[0] Snickers"
        # Create a second loop that runs for a set number of times determined by the variable allowance.

        # For example: If allowance is equal to five, the loop should run five times.

        # Each time this second loop runs, take in a user's input, preferably a number, and then add the candy with the matching index to the variable candy_cart.

        # For example: If the user enters "0" as their input, "Snickers" should be added into the candy_cart list.

        # Use another loop to print all of the candies selected to the terminal.

        # Bonus
        # Create a version of the code that allows a user to select as much candy as they want until they say they do not want any more.

React

Reply


