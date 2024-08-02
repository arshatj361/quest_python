'''
Accpet a string of space seperated numbers and store them as a matrix (list of lists) of n rows.
Now print the matrix row-wise
'''
input_string = input("Enter numbers with space separation: ")
num_rows = int(input("Enter the number of rows: "))

def create_matrix_from_input(input_string, num_rows):
    numbers = [int(num) for num in input_string]
    
    # Calculate the number of columns based on the total number of elements and rows
    num_elements = len(numbers)
    num_cols = num_elements // num_rows
    
    
    matrix = []
    for i in range(num_rows):
        row_start = i * num_cols
        row_end = row_start + num_cols
        matrix.append(numbers[row_start:row_end])
    
    return matrix

def print_matrix(matrix):
    for row in matrix:
        print(row)



matrix = create_matrix_from_input(input_string, num_rows)
print("Matrix:")
print_matrix(matrix)