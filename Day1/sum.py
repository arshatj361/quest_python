n=int(input('enter the number you want to multiply'))
m=int(input('enter the limit'))

def series_sum(n, m):
    total_sum = 1  
    sign = 1       
    for i in range(1, m):  
        if sign > 0:
            total_sum += n * i
        else:
            total_sum -= n * i
        
        sign *= -1