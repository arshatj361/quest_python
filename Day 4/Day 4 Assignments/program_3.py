#Accept N strings, and check howmany of them possess the string X

def count_x_in_string(N, X, strings):
    count = 0
    for string in strings:
        if X in string:
            count += 1
    return count

N = int(input("Enter the number of strings: "))
X = input("Enter the X value to search for: ")
strings = [input("Enter string {}: ".format(i + 1)) for i in range(N)]

result = count_x_in_string(N, X, strings)
print("Number of strings containing '{}': {}".format(X, result))