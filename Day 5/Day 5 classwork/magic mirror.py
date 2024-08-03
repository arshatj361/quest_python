#rotate the input string and chec the rotated string is the rotation of original string or not

def is_rotation(original, rotated):
    if len(original) != len(rotated):
        return False
    doubled_original_string= original + original
    
    return rotated in doubled_original_string

original_string = input('Enter the original string: ')
rotated_string = input('Enter the rotated string to check: ')

if is_rotation(original_string, rotated_string):
    print('Yes, the rotated string is a rotation of the original string.')
else:
    print('No, the rotated string is not a rotation of the original string.')
