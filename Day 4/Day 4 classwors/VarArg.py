def varArgFunction1(*arguments):
    print(arguments)
    print(type(arguments)) # tuple
 
def varArgFunction2(*arguments):
    for i in range(len(arguments)):
        print(arguments[i])
 
varArgFunction1(1, 2, 4)
varArgFunction1()
varArgFunction1('list', 'tuple', 'set', 'dictionary')
 
varArgFunction2(1, 2, 4)
varArgFunction2()
varArgFunction2('list', 'tuple', 'set', 'dictionary')
 
''''
def varArgFunction2(*arguments):
        print(arguments)
 
def varArgFunction2(*arguments):
    for i in range(len(arguments)): #Loop with range() function
        print(arguments[i])
 
def varArgFunction2(*arguments):
    for element in arguments: # for each loop. It accesses all elements of the tuple one by one
        print(arguments[i])
'''