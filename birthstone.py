# Follow the assignment instructions to code an app that
# will tell a user their birthstone.
#Ask the user “Enter the number of the month you were born (1-12) ” 

#Convert user_input to an integer using int() and store the value in a variable called month
month=''
while month != 0:
    # Store the answer in a variable called user_input.
    user_input = input("Enter the number of the month you were born (1-12) or '0' to quit >")
    month=int(user_input)
    if month == 1:
        print("Your birthstone is garnet.")
    elif month == 2:
        print("Your birthstone is amethyst.")
    elif month == 3:
        print("Your birthstone is aquamarine.")
    elif month == 4:
        print("Your birthstone is diamond.")
    elif month == 5:
        print("Your birthstone is emerald.")
    elif month == 6:
        print("Your birthstone is pearl.")
    elif month == 7:
        print("Your birthstone is ruby.")
    elif month == 8:
        print("Your birthstone is peridot.")
    elif month == 9:
        print("Your birthstone is sapphire.")
    elif month == 10:
        print("Your birthstone is opal.")
    elif month == 11:
        print("Your birthstone is topaz.")
    elif month == 12:
        print("Your birthstone is turquoise.")
    else:
       break

