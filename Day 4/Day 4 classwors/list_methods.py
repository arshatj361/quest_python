numbers = [1, 2, 3, 4, 5]
del numbers[1:3]
print(numbers) # [1, 4, 5]
del numbers[1]
print(numbers) # [1, 5]
del numbers[:] # we are deleting all the elements from the list
print(numbers) # []
numbers.insert(10, 0) # inserting the element 10 at index 0