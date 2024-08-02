# Program to find the smallest and largest number in a list

def largest_number(list):
    largest_number=max(list)
    return largest_number

def smallest_number(list):
    smallest_number=min(list)
    return smallest_number

N = int(input("Enter the number of elements: "))
list = []

for i in range(N):
    number = int(input("Enter the numbers in the list: ")) 
    list.append(number)

print("the largest number is", largest_number(list))  
print("the smallest number is", smallest_number(list))

