

"""
Stupid Loops Lecture

There are two types of Loops in Python:

For Loop - For loops are used when you know how many times you want to interate through a list or objects

While Loop - The While loop is used when you don't know how many times you want to iterate through a list but
             iterates until the condition is no longer true.

________________________________________________________________________________________________________________________

There are three control keys:

Break - Will stop the loop entirely

Continue - Will skip the object in the loop when found

Pass - Does nothing and is just a placeholder.

------------------------------------------------------------------------------------------------------------------------

"""

# loop practice: Count from 1 to 10 using a for loop
# Print the numbers 1 to 10: HINT: Use range(start, end). Remeber, rang(1,11) goes from 1 to 10(the end is excluded)

#Example of a for loop and a range()
for number in range(1,11):
    if number == 5:
        print(" \t skiped 5 here becuase we are using the continue control key..")
        continue

    print("Number:", number)



# loop practice: Count down from 10 to 1 using a while loop and print  "Blast off!", at the end
#HINT: Start with a variable to intialize then used the while loop with the  >0 operater

# to count down, start with a condition:
countdown = 10

while countdown > 0:
    print(countdown)
    countdown -=1

print("Blast OFF!! cause you got this!! ** this is out of the loop. ")



# loop challenge - Skip number 7 while counting from 1 to 10
# use a for loop and continue to skip the number 7

for num in range(1,11):
    if num == 7:
        print("\t skip number 7 here..")
        continue
    else:
        print("the number is: ", num)





#-----------------------------------------------------------------------------------------------------------------------
"""
Loops and inputs - when put together are powerful and interactive programs 

this sections taught me the following:

How to collect input from a user
How to use input in a loop
How to stop a loop based on user input 




What is input in Python: 
This is a python function that allows a user to insert data. 
The input() WILL ALWAYS RETURN A STRING

"""
#-----------------------------------------------------------------------------------------------------------------
"""
What I learned from this code example
1: Case Sensitivity in the if Chacker:
* If you're using .upper() to check an input, then the answer as to be an upper as well. 

2: input("Whats your name again?") is not saved to the name variable.

3: You're using .lower() on a print() statement, which doesn’t work.
"""
# example

# this is an example fo the input()
name = input("Enter your name: ")

# Now, Ask for a confirmation with more input
confirm = input(f"Hey, your name is {name}. Is this right? (Yes or No): ").lower()    # can be .lower()  too!

# heres the branching part, watch your indentations
if confirm == "yes":
    print(f"Your name is {name} ")
### the else statement has to match the space of the if statement
else:
    # Get the correct name:
    name = input(f"Sorry, whats your name again?").lower()
    print(f"Hello {name}")



#-----------------------------------------------------------------------------------------------------------------------

# this exercise teaches me 1: how to store numbers into a list 2: Calculate the total(sum) 3: Optionall find the average in a list

# step one, to store numbers or any data into a list (a container).. you need to create a list (a container)
numbersList = []  # this is an empty list


#step2: This is how to use a for loop to iterate through a a range of 5 elements
for i in range(5):     # for the loop, with the counter i in a range of 0-4
    number = int(input(f"Enter a number {i +1}: "))       # get an input from the user
    numbersList.append(number)    # add the input into the list


# Notice we are out of the loop~
# print all the numbers in the list
print("You have entered: ", numbersList)



# to calculate the sum (the total value in the list)
total = sum(numbersList)# to calculate the average value in the list
avgValue = total/len(numbersList)     # gives the number of items (so we can find the average).

print("the average value in the list is ", round(avgValue,2))    #rounds the result to 2 decimal places.
print(f"The total value in the list is: ", total)


#-------------------------------------------Nested Loops--- ----------------------------------------------------------

# this is an example of a loop
for i in range(5):
    print("I will pick up 5 marbels")



# what is a nested loop? Example of a nested loop
"""
Image you have 2 boxes, and each box has 4 toys inside.
You want to pick up each toy from each box.

so you:
1: open the first box, pick up the 4 toys
2: open the second box, pick up 4 toys

This is a nested loop. The boxes are the outer loop, pickig up the 4 toys are the inner loop

in code it will look like this: 

"""

for box in range(2):     # this is the outter loop
    print("Open box", box + 1)    # do something
    for toy in range(4):       # this is the inner loop
        print("pick up", toy+1, "toy")  # do something


"""
Remember: Nested loops will help you:

1: work on grids, patterns, and games
2: Do tasks within a tasks
3: Go row by ros and column by column

"""