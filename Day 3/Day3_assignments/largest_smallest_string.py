

def smallest_string(string):
     smallest = string[0]

     for s in string:
        if len(s) < len(smallest):
            smallest = s
     return smallest
def largest_string(string):
     largest = string[0]

     for s in string:
        if len(s) > len(largest):
            largest = s

     return largest

   
N=int(input("enter the number of string: "))

string=[]

for i in range(N):
    s = input("Enter the strings in the list: ")
    string.append(s)

print("the largest string is", largest_string(string))  
print("the smallest string is", smallest_string(string)) 
