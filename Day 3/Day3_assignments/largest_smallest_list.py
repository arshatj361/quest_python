def main():
    
    N = int(input("Enter the number of elements: "))
    
    
    numbers = []
    
    
    for i in range(N):
        num = int(input(f"Enter number: "))
        numbers.append(num)
    
    
    if numbers:
        
        smallest = numbers[0]
        largest = numbers[0]
        
        
        for num in numbers:
            if num < smallest:
                smallest = num
            if num > largest:
                largest = num
        
        
        print("Smallest element:", smallest)
        print("Largest element:", largest)
    else:
        print("The list is empty!")