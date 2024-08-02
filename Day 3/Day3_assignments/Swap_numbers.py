#Accept N numbers from the user and swap the consecutive element in the list

def swap_consecutive_elements(list):
    for i in range(0, len(list) - 1, 2):
        list[i], list[i + 1] = list[i + 1], list[i]
    return list

N= int(input("Enter the number of elements: "))

list = []
for i in range(N):
    num = int(input("Enter the numbers in the list: "))
    list.append(num)

swapped_consecutive_numbers = swap_consecutive_elements(list)

print("\nList after swapping consecutive elements :")
print(swapped_consecutive_numbers)