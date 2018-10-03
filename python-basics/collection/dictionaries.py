
def dictionaries():
    #Definine a dictionary
    tel = {'jack': 4098, 'sape': 4139}
    print(tel)

    #Update
    tel['jack']=1234
    print(tel)

    #Delete an element
    del tel['sape']
    print(tel)

    #Add an element
    tel['irv'] = 4127
    print(tel)

    #Get all keys 
    print(list(tel))

    #Get all keys sorted
    print(sorted(tel))

    if 'jack' in tel:
        print(True)

    if 'jack1' not in tel:
        print(False)

    #The dict() constructor builds dictionaries directly from sequences of key-value pairs:
    dicts=dict([('sape', 4139), ('guido', 4127), ('jack', 4098)])
    print(dicts)

    #dict comprehensions can be used to create dictionaries from arbitrary key and value expressions:
    dict2={x: x**2 for x in (2, 4, 6)}
    print(dict2)

    #When the keys are simple strings, it is sometimes easier to specify pairs using keyword arguments
    dict3=dict(sape=4139, guido=4127, jack=4098)
    print(dict3)

    print("*****Loop through dictionary.")
    for k,v in dict3.items():
        print(k,v)

#Invoke test functions
dictionaries()