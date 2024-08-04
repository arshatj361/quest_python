List Slicing:
 
numbers = [2, 9, 7, 5, 3, 13, 19, 17, 29]
print(numbers) # we get the complete list
print(numbers[0]) # we get the 1st element
print(numbers[-1]) # we get the last element
Hence, we see that -ve indexing is possible in Python
print(numbers[-2]) # we get last but element from the list
print(numbers[:]) # we get the complete list
Here, we have written nothing before the colon and hence it is treated as 0, which means start from the beginning of the list. Here also have not written anything after the colon, which means it is treated as UP TO END OF THE LIST. 
print(numbers[:3]) # Start from index 0 and access elements up to index 3-1 which is 2.
print(numbers[1:-1]) # Start from index 1 (2nd element) and access elements up to last but element, because -1 is the index of last element and we must not include it.
print(numbers[1:8:2]) # start from index 1 and access upto index 8-1 and increment each time by 2 elements. So o/p is [9, 5, 3, 19]
print(numbers[::3]) # start from biginning and go up to end of the list with increment of 3
print(numbers[8:1:-2]) Start from index 8, go up to index 2 with decrement of 2 (or increment of -2)
print(numbers[::-1]) # Since the increment is negative, we understand that we have to move in reverse (meaning from the end to towards the start). The area within the list we have to access is all the elements, because nothing is specified before and after the 1st colon :
has context menu

_____________________________________________________________________________________________________

More on Lists
The list data type has some more methods. Here are all of the methods of list objects:

list.append(x)
Add an item to the end of the list. Equivalent to a[len(a):] = [x].

list.extend(iterable)
Extend the list by appending all the items from the iterable. Equivalent to a[len(a):] = iterable.

list.insert(i, x)
Insert an item at a given position. The first argument is the index of the element before which to insert, so a.insert(0, x) inserts at the front of the list, and a.insert(len(a), x) is equivalent to a.append(x).

list.remove(x)
Remove the first item from the list whose value is equal to x. It raises a ValueError if there is no such item.

list.pop([i])
Remove the item at the given position in the list, and return it. If no index is specified, a.pop() removes and returns the last item in the list. It raises an IndexError if the list is empty or the index is outside the list range.

list.clear()
Remove all items from the list. Equivalent to del a[:].

list.index(x[, start[, end]])
Return zero-based index in the list of the first item whose value is equal to x. Raises a ValueError if there is no such item.

The optional arguments start and end are interpreted as in the slice notation and are used to limit the search to a particular subsequence of the list. The returned index is computed relative to the beginning of the full sequence rather than the start argument.

list.count(x)
Return the number of times x appears in the list.

list.sort(*, key=None, reverse=False)
Sort the items of the list in place (the arguments can be used for sort customization, see sorted() for their explanation).

list.reverse()
Reverse the elements of the list in place.

list.copy()
Return a shallow copy of the list. Equivalent to a[:].

____________________________________________________________________________________________

Global methods and keywords:
numbers = [1, 2, 3, 4, 5]
del numbers[1:3]
print(numbers) # [1, 4, 5]
del numbers[1]
print(numbers) # [1, 5]
del numbers[:] # we are deleting all the elements from the list
print(numbers) # []
numbers.insert(10, 0) # inserting the element 10 at index 0
 
INSERT ELEMENT AT REAR OF THE LIST: 3 different ways
a.insert(len(a), x)
a.append(x)
a.[len(a):] = [element]
 
Below is an error
numbers[len(numbers):] = 3
TypeError because we must assign only a list(itarable) not a primitive value
_________________________________________________________________________________

name = 'Cambodia'
 
names = ['aizwal', 'imphal', 'shillong', 'agartala']
 
print(name)
print(name.upper())
print(name.count('a'))
print(name.count('A'))
print(name.upper().count('A'))
print(name.upper().count('a'))
print(name.find('o'))
print(name.find('dia'))
print(name.find('xx'))
____________________________________________________________________________________________________



_______________________________________________________________________________________________________

l1 = [3, 6, 10]
l2 = [1, 2, 4, 12]
 
if l1 > l2:
    print('List1 is bigger')
else:
    print('List2 is bigger')
   
if l1.__gt__(l2):
    print('List1 is bigger')
else:
    print('List2 is bigger')
 
'''
For readability purpose we use 6 R.oprs
> < >= <= != ==
However we can perform any of the 6 operations using:  > and ==
'''

__________________________________________________________________________________________________________

DS of python

___________________________________________________________________________________________________________

list1 = []
list1 = list()
tuple1 = ()
tuple2 = tuple()
dictionary1 = { }
dictionary2 = dict()
set1 = set()
print(type(dictionary1))
print(type(set1))
print(type(tuple1))

______________________________________________________________________________________________________________

Variable argument function

___________________________________________________________________________________

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
#____________________________________________________________________________________________________________________

def varArgFunction1(*arguments):
    print(arguments)
    # arguments[1] = 22 # TypeError
    arguments[5][0] = 20 # even though the list is inside the tuple, we can modify it.
    print(arguments)
    arguments[5].append(50)
    print(arguments)
 
varArgFunction1(1, 2, 4, 'list', 4.5, [2, 3, 5])

#______________________________________________________________________________________________________________________


Problems:
1. User gives the data like this:
kerala-tiruvanantapuram karnataka-bengaluru tamilnadu-chennai
You have to separate the states and store in the list states[] and also the seperated capitals must be stored in capitals[]
 
2. Accpet a string of space seperated numbers and store them as a matrix (list of lists) of n rows.
Now print the matrix row-wise
 
3. Accept N strings and count the number of Palindromes in it.
 
4. Accept N strings, and check howmany of them possess the string X
 
5. Accept N main strings and N sub strings into lists and check create a list of numbers of 0s and 1s where 0 represents that the sub string at respective index is not a substring of the main string.
 
main_list = ['andhra pradesh', 'kerala', 'maharashtra', 'haryana']
sub_list  = ['pradesh', 'south', 'rashtra', 'punjab']
 
presence = [1, 0, 1, 0]

