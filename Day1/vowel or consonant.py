#check if a number is vowel or consonant
#ALGORITHM
#Enter the input string
#The string is converted to lower case by the function letter.lower().Because we a giving the set of vowels in lower case
#then check the input is a letter or a word by checking the length
#put vowels in a set
#then check the given vowel is in this set or not



input_letter=input('enter the letter  ').lower()
vowels={'a','e','i','o','u'}

if len(input_letter)!=1:
    print('enter an alphabet')

elif input_letter in vowels:
    print('The given letter is vowel')

else :
    print('The given letter is not vowel')
