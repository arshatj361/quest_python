def check_if_prime(n):
    for i in range(2, math.ceil(math.sqrt(n))+1):
        if n % i == 0:
            return False
    return True

def find_nth_fibo_term(n):
    thrid_number = 0
    first_number  = 1
    second_number = 2  
    if n == 1:
        thrid_number = 1
    elif n == 2:
        thrid_number = 2
    else:
        thrid_number  = 0
        count = 2
        while count <= n:
            thrid_number = first_number + second_number
            count += 1
            if count == n:
                return thrid_number
            first_number  = second_number
            second_number = thrid_number
    return thrid_number
N=int(input("enter the numner"))
while N>0:
if (i + 1) % 2 != 0:
    print("the number is",check_if_prime(n))
else:
    print("the number is",find_nth_fibo_term(n))
    