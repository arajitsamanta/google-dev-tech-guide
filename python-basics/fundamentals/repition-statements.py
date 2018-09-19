
def whileLoop():
    theSum = 0
    i = 1
    while i <= 100:
        theSum = theSum + i
        i = i + 1
    print("The sum = ", theSum)

    #The while loop is a compound statement and thus requires a statement block even if there is only a single statement to be executed. Consider the user of 
    #the while loop for user input validation
    value = 0
    while value < 0 :
        value = int(input("Enter a postive integer: "))

#The for loop in Python is more than a simple construct for creating general count-controlled loops as in Java. Instead, it is a generic sequence iterator that can 
#step through the items of any ordered sequence object. The general syntax of the for loop is as follows
#   for <loop-var> in <object> :
#       <statement-block>
#The body of the loop (statement-block) is executed once for each item in the ordered sequence. Before beginning each iteration, the current item of the ordered
#sequence is assigned to the loop variable (loop-var).
def forLoop():
    #single step iteration
    for i in range( 1, 11 ):
        print(i)

    #variable step increments
    #Instead of stepping or counting by 1, a third argument can be provided to the xrange() function to indicate the step value.
    for i in range( 0, 51, 5 ):
        print(i)
    #Iterationg from zero
    #Incrementing loops which start with an index of 0 are very common. Therefore, the xrange() function has a special version which starts at 0 and iterates a
    #specified number of times. In the following example,
    for i in range(20):
        print(i)

#Reads a group of positive integer values from the user,
#one at a time, until a negative value is entered. The average
#value is then computed and displayed.
def avgValue():
    # Initlize the counting variables.
    total = 0
    count = 0

    # Extract the values.
    value = int(input("Enter an integer value (< 0 to quit): "))
    while value >= 0 :
        total = total + value
        count = count + 1
        value = int(input("Enter an integer value (< 0 to quit): "))

    # Compute the average.
    avg = float( total ) / count

    # Print the results.
    print("The average of the", count, "values you entered is", avg)

#This program iterates through a string and counts the number of vowels it contains.
def countVowels():
    # Extract a string from the user.
    text = input( "Enter a string to be evaluated: " )

    # Iterate through the string.
    numVowels = 0
    vowels="aeiou"
    for ch in text :
        if ch in vowels:
            numVowels = numVowels + 1

    # Print the results.
    print("There are " + str( numVowels ) + " vowels in the string.")

#invoke test functions
whileLoop()
forLoop()
avgValue()
countVowels()