# 1. Read a number say 'n'
# 2. Find the square root of 'n'
# 3. Take the produt of squareroot
# 4. If the product of square root is equal to n , then print the given number is a perfect square
# 5. else print the number is not a perfect square

import math  
num = int(input('enter the number') )
r=math.sqrt(num)
a=round(r)
if a*a==num:
   print('perfect num')
else:
   print('not perfect num')
   
