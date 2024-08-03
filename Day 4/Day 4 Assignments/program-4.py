def mainstrings_and_substrings():
    N = int(input("Enter the number of strings: "))   
    
    mainstrings = []
    substrings = []

    print(f"Enter {N} main strings:")    
    for i in range(N):
        main_string = input(f"Main string {i + 1}: ")
        mainstrings.append(main_string)   

    print(f"Enter {N} substrings to search for:")
    for i in range(N):
        substring = input(f"Substring {i + 1}: ")
        substrings.append(substring)        

    return mainstrings, substrings

def presence_sub_in_main(main_strings, substrings):
    presence = []
    
    