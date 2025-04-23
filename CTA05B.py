# part 2:
# sara khon 04/23/2025

student = 0

while True:
    # get the user input
    books_Purchased = int(input("Enter the number of books purchased this month: "))

    if books_Purchased < 2:
        points = 0
        print("You have earned O points")
    elif books_Purchased < 4:
        points = 5
        print("You have earned 5 points")
    elif books_Purchased < 6:
        point = 15
        print("You have earned 15 points")
    elif books_Purchased < 8:
        point = 30
        print("You have earned 30 points")

    else:
        point = 60
        print("You have earned 60 points this month! YAY! ")

    # Ask the user if they want to exit the application
    answer = input("Do you want to exist the application? (yes or no) )").lower()

    if answer !="no":
        print("Goodbye!")
        break     # stop the while loop, end the application





