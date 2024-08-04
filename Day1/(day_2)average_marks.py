#print fail if 0<=mark<=49, second class if 50<=mark<=54, first class if 75<=marks<=89 and distinction if 90<=mark<=100




average_score =int(input('enter average score: '))
if (average_score>=0 and average_score<=49):
    print('fail')
elif (average_score>=74):
    print('second class')
elif (average_score>=90):
    print('first class')
elif(average_score>=100):
     print('Distinction')
else:
    print('invalid input')