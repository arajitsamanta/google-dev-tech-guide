
# Some functions are very common and are part of the Python language itself These built-in functions are considered to be
# global to the program. Thus, they are always available and can be invoked using only the function name.
# When passing parameters to a function, the reference to the object is passed and not the value itself. This is the
# expected behavior since Python represents all data as objects and all variables contain references


def builtinFunc():
    # Compute the absolute value of the integer x
    y = abs(-1.5)
    print(y)

    # Create a complex number with real value r and imaginary i.
    z = complex(5, 6)
    print(z)


def userDefinedFuncWithReturnVal(x):
    return x**x

# Arguments in Python are passed by value and in the order specified. Since every value is an object, these values are always object references. The formal
# arguments defined for a function become aliases of the actual parameters passed to the function which it’s called.
# Passing the reference to a mutable argument to a function allows that object to be modified by the function. Immutable objects can not be modified within a
# function and is similar to passing Java primitive types “by value”.


def sumRange(first, last):
    total = 0
    i = first
    while i <= last:
        total = total + i
        i = i + 1
    return total

# Python allows functions to be defined with default argument values. For example, we can add a third argument to the sumRange() function to specify the step value.


def sumRange2(first, last, step=1):
    total = 0
    i = first
    while i <= last:
        total = total + i
        i = i + step
    return total


builtinFunc()
print(userDefinedFuncWithReturnVal(4))
start = 1
end = 100
theSum = sumRange(start, end)
print("The sum of the integers between", start,
      "and", end, "is", theSum)

# ***** Polymorphism *****
"""
Python is a dynamically typed language with polymorphism everywhere. In fact, every operator in Python is a polymorphic operation. Polymorphism also plays a role with
function arguments.

As you have noticed, data types are not specified for function arguments. So, what keeps us from passing floating-point values into the sumRange() function? Consider 
the following example
"""
print(sumRange(1.37, 15.78))
"""
which is a valid statement call in Python. So long as all operations within the function can be applied to the given values, the program will execute correctly. 
If an operation can not be applied to a given argument type, an exception will be raised to indicate the invalid type.
"""

# ***** Default Values *****
"""We have also provided a default value for the step argument. If the value of the third argument is omitted when calling the function as with the original function.
Deafult argument should always be the last one in function definition.
Invoke sumRange2 with no 3rd argument
"""
print("Invoke function with missing last argument", sumRange2(1, 100))

# ***** Keyword Arguments *****
"""As in Java and most other languages, Python passes arguments to functions in the order they were specified. But Python also allows you to specify the argument
order by using keyword arguments. Consider the following function call in which we directly specify which argument is suppose to receive which value.
"""
print(sumRange2(last=100, step=3, first=1))


# ***** Return value *****
"""
All functions in Python return a value whether you specify one or not. The return statement is used to terminate a function and return a value or more specifically
to return an object reference. If you omit the return statement, Python automatically returns a reference to the None object.

Most functions return a single value, but you can define functions that return multiple values by returning those values within a tuple.
"""

# ***** Function as Arguments *****
"""
While the def keyword is used to define a Python function, it is actually a statement which is executed by the interpreter. When Python executes a def statement,
a function object is created containing the statments within the body of the function. The function name is actually a variable to which the function object is
assigned.The statements within a function are not executed until the function is called even though the statements are interpreted an converted to byte-code
as they are read. Therefore, you can refer to one function within another before the former has been defined. Consider the following code segment
The order in which functions are listed within a file is not important, but the order of executable statements at file level is. Some people find it helpful to
place the top-level statmentes within a single driver function and then call this function at the end of the file. Other functions used to subdivide the problem
would be placed between the driver function and the call at the end of the file as illustrated in the following example.
"""
# Simulate the rolling of two dice using the random number generator.

from random import randint

# Minimum number of sides on a die
MIN_SIDES = 4

# Our very own main routine for a top-down design.
# This is not a standard function in Python.


def main():
    print("Dice roll simulation.")
    numSides = int(
        input("How many sides should the die have? "))

    if numSides < MIN_SIDES:
        numSides = MIN_SIDES
    value = rollDice(numSides)
    print("You rolled a", value)

# Simulate the rollowing of two nSided dice.


def rollDice(nSides):
    die1 = randint(1, nSides + 1)
    die2 = randint(1, nSides + 1)
    return die1 + die2


# Call the main routine which we difined as the first
# function in the file.
main()
