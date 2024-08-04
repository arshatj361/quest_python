N = int(input("Enter the number of elements: "))
list = []

for i in list:
    if i<0:
       list.remove(i)
for i in range(N):
    number = int(input("Enter the numbers in the list: ")) 
    list.append(number)


print("list after removing negative numbers",list)