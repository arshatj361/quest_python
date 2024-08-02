#Accept N numbers from the user and swap the consecutive element in the list

def main():
    N = int(input("Enter the number of elements: "))
    numbers = []
    for i in range(N):
        num = float(input(f"Enter number {i + 1}: "))
        numbers.append(num)
    
    for i in range(1, N, 2):
        numbers[i-1], numbers[i] = numbers[i], numbers[i-1]
    
    print("List after swapping consecutive elements:")
    print(numbers)

