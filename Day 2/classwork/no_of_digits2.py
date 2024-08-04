#Alternative Program to count the number of digits in a number

input_number = int(input('Enter a number to count number of digits in it: '))

count_of_digits = len(str(input_number))

print(f'Number of digits in {input_number} is {count_of_digits}')