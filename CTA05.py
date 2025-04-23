
"""
Student: Sara khon Module 5: Critical Thinking Assignment Date 04/22/2025
"""

# Part: 01

# Will be used to track the total rainfall abd total numbers of months
total_months = 0
total_rainFall = 0


# ask the user to input the number of years,
years = int(input("Enter the number of years: " ))   # convert str to int


# Using a for loop for the outer loop to iterate once a year
for year in range(1, years +1):      # add the 1 in the 1st parameter so it starts @1 and not 0 // Add the +1 to include the final year
    print(f"Year:{year}")

    for month in range(1,13):        # start of the inner loop
        while True:
            try:
                rain = float(input(f" Enter the amount of rainfall (in inches) for month {month}: "))
                if rain <0:
                    print( "ERROR - Entered a non-negative number. Try again.")
                    continue
                break
            except ValueError:              # handles value error
                print(  "Enter a valid value (IN INCHES)")

        total_rainFall +=rain
        total_months +=1


# gets the average rainfall for the entire period
average_rainFall = total_rainFall/total_months

# prints out the work
print("\n -- Rainfall Summary --")
print("Displaying - Total Number of Months: ", total_months)
print("Displaying - Total Inches of rainfall: {:.2f} inches".format(total_rainFall))
print("Displaying Average rainfall for the Entire Period: {:.2f} inches".format(average_rainFall))






