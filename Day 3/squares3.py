import math
squares3 = list(map(lambda x: ((x**2) + int(math.sqrt(x))), range(10)))
print('Squares3 = ', squares3)
 
input_numbers = list(map(int, input().split()))
print(input_numbers)