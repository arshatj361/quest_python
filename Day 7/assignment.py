s1=input("enter the string1: ")
s2=input("enter the string2: ")
n1=int(input("enter the number1: "))
n2=int(input("enter the number2: "))

def string_num(s1,s2,n1,n2):
    try:
        joined_string=s1+s2
        result_sum = n1+n2
        return joined_string,result_sum
    except Exception as e:
	    print('Some Error occured')
