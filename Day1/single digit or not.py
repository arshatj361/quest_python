#Check whether he number is single digit or not

#ALGORITHM

#enter a number
#check if it is between 0 to 9 .Because single digits are fron 0 to 9
#If yes print the number is one digit
#else print not one digit number


n=int(input('enter the number: '))
if 0<=n<=9:
    print('The number is single digit')
else:
     print('The number is not single digit')
