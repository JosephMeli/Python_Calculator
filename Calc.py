

def help():
    print(
    "** Add: Takes one varible x and one varible y. Then sums the two varibles and returns this value."
    "** Subtract: Takes one varible x and one varible y. Then takes the difference of the two varibles and returns this value."
    "** Multiply: Takes one varible x and one varible y. Then gets the product of the two variables and returns the result."
    "** Divide: Takes one varible x and one varible y. Then takes quotient of these two variables and returns the result."
    "** PercentOf: Takes the two given variables and uses the first number to define the Percent you wish to find and the second number, is the whole number you are finding the percent of. Returns the final percent of the number you wish."
    )
    start()

#Basic Operations
def add(x,y):
    print x + y
    start()

def subtract(x,y):
    print x - y
    start()

def mutiply(x,y):
    print x * y
    start()

def divide(x,y):
    print x / y
    start()

#this fucntion wokrs as if x = Percent you wish to find
# so if you wnated to find 10% of 75
# x = 10 and y = 75 for this function implmentation
def percentOf(x,y):
    return (x/100) * y
    start()
    
def calculate(x,y,z):
    if (z == 1) : add(x,y)
    elif (z == 2) : subtract(x,y)
    elif (z == 3) : mutiply(x,y)
    elif (z == 4) : divide(x,y)
    elif (z == 5) : percentOf(x,y)
    elif (z == 6) : help()
    elif (z == 99) : exit()
    else : start()


def start():
    usrNum_1 = float(input("Enter the first number:"))
    usrNum_2 = float(input("Enter the second number"))
    print("Select 1 for Add")
    print("Select 2 for Subtract")
    print("Select 3 for Multiply")
    print("Select 4 for Divide")
    print("Select 5 for Percent Of")
    print("Select 6 for Help")
    print("Select 99 for Quit")
    operation = int(input("Select an operation"))
    calculate(usrNum_1,usrNum_2,operation)

start()
