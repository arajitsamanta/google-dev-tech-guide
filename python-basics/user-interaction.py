
# In python, there is a single function for extracting data from the user. The following Python code segment reads from standard
# input device. The input() function waits for the user to enter a line of data at the keyboard, terminated with a carriage return.
# The data entered by the user is then returned as a string. In this example, if the user enters Smith at the keyboard, name will 
# refer to the string "Smith".
def standardInput():
    print ("What is your name? ")
    name = input()
    print (name)

    # When extracting data from the user, we typically prompt the user with a message indicating what should be entered. 
    # Since this is so common, Python allows an argument to be passed to the input() function to be used as a prompt. 
    # We can rewrite the previous example as
    name = input("What is your name? ")
    print (name)

    # for anything other than string to need to manually convert input to appropriate data type. for e.g. below we convert it to float
    # using predefined float() function.
    numeric_type=input("Whats your gpa ?")
    gpa = float(numeric_type)
    print (gpa)

    # above can be written as gpa=float(input("whats your goa ?"))

def standardOutput():
    avg = 4.5 / 3.0
    print("Your average grade = ",avg)

# Computes the taxes and wages for an employee given the
# number of hours worked and their pay rate.
def calculateWages():
    # wages.py
    # Set tax rates as constants.
    STATE_TAX_RATE = 0.035
    FED_TAX_RATE = 0.15

    # Extract data from the user.
    employee = input( "Employee name: " )
    hours = float( input( "Hours worked: " ) )
    payRate = float( input( "Pay rate: " ) )

    # Compute the employee's taxes and wages.
    wages = hours * payRate
    stateTaxes = wages * STATE_TAX_RATE
    fedTaxes = wages * FED_TAX_RATE
    takeHome = wages - stateTaxes - fedTaxes

    # Print the results.
    print ("PAY REPORT")
    print ("Employee: ", employee)
    print ("----------------------------------")
    print ("Wages:       ", wages)
    print ("State Taxes: ", stateTaxes)
    print ("Fed Taxes:   ", fedTaxes)
    print ("Pay:         ", takeHome)

def formattedOutput():
    print ("The sum of %d and %d is %f\n" % (5, 6, 11))

#Tnvoke test functions
#standardInput()
#standardOutput()
#calculateWages()
formattedOutput()