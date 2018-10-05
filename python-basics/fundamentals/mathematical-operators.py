def operators():
    print ("Modulus %:", 5 % 6)
    print ("Divison /:", 5/6)
    print ("Multiplication *:", 5*6)
    print ("Addition +:", 5+6)
    print ("Subtraction -:", 5-6)
    print ("Exponential **:", 5**6)
    print ("Floored: Floor", 7//6)

# Mixed Types
# If the two operands are of the same type (i.e. float), the type of the resulting value will be the same; if they are different, the operand of lesser rank will
# be converted to the higher rank. The conversion is only temporary for use in the evaluation of the given operator; the actual object is not modified. In Python, t
# he ranks of the numeric types are

# int > long > float > complex

# Type Conversions
# Python will implicitly convert between the numeric types as needed. All other conversions, however, must be explicit. Python provides a number of built-in functions
# to handle these conversions. Descriptions and examples will be provided in the following chapters.


# call functions
operators()
