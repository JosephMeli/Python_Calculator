#!usr/bin/python3


should_Continue = True
usrNum_1 = 0
usrNum_2 = 0


def help():
    print("""** Add: Takes one varible x and one varible y. Then sums the two
    varibles and returns this value.
    ** Subtract: Takes one varible x and one varible y. Then takes the
    difference of the two varibles and returns this value."
    ** Multiply: Takes one varible x and one varible y. Then gets the product
    of the two variables and returns the result.
    ** Divide: Takes one varible x and one varible y. Then takes quotient of
    these two variables and returns the result."
    ** PercentOf: Takes the two given variables and uses the first number to
    define the Percent you wish to find and the second number, is the whole
    number you are finding the percent of. Returns the final percent of the
    number you wish."
    """)

# Basic Operations


def add(x, y):
    result = x + y
    return result


def subtract(x, y):
    result = x - y
    return result


def mutiply(x, y):
    result = x * y
    return result


def divide(x, y):
    result = x / y
    return result

# this fucntion wokrs as if x = Percent you wish to find
# so if you wnated to find 10% of 75
# x = 10 and y = 75 for this function implmentation


def percentOf(x, y):
    result = (x/100) * y
    return result


def calculate_Choice(x, y, z):
    if(z == 1):
        print(add(x, y))
    elif(z == 2):
        print(subtract(x, y))
    elif(z == 3):
        print(mutiply(x, y))
    elif (z == 4):
        print(divide(x, y))
    elif (z == 5):
        print(percentOf(x, y))
    elif(z == 6):
        help()
    else:
        print "That is not a valid option"

# use to sanatize the operation input from the user


def sanatize_OperationChoice(a):
    if(a < 1 and a > 6):
        print("operation choice not valid")
        return False
    else:
        return True

# For sanatizing input of numbers

valid = False

# main loop used to run the program until user wishes to quit
while (should_Continue):
    # checks for valid input of a float or integer

    while not valid:
            try:
                usrNum_1 = float(raw_input("Enter the first number: "))
                usrNum_2 = float(raw_input("Enter the second number: "))
                valid = True
            except ValueError:
                print("Please enter a number.")
                valid = False
    print("Select 1 for Add")
    print("Select 2 for Subtract")
    print("Select 3 for Multiply")
    print("Select 4 for Divide")
    print("Select 5 for Percent Of")
    print("Select 6 for Help")
    print("Select 99 for Quit")
    operation = int(input("Select an operation: "))
    if(operation == 99):
        print("Goodbye!")
        should_Continue = False
    elif(not sanatize_OperationChoice(operation)):
        print("invalid operation choice")
    else:
        calculate_Choice(usrNum_1, usrNum_2, operation)
