branch = input("1. ECE\n2. BCOM\n3. MECH\nEnter your branch: ").strip()
Arts = int(input("Enter your marks in Arts: "))
Maths = int(input("Enter your marks in Maths: "))
Literature = int(input("Enter your marks in Literature: "))

preference = input("1. Arts\n2. Maths\n3. Literature\nEnter your preferences with commas: ").strip()


split_inputs = preference.split(',')
preference_list = [int(item) for item in split_inputs]


if branch == "1":  # ECE
    if Arts > 90 and Literature > 90 and Maths > 35:
        if 1 in preference_list or 3 in preference_list: #1.arts 3. literature.
            print("You are eligible for Marketing")
    else:
        print("You are not eligible for Marketing")

    

elif branch == "2":  # BCOM
    if Maths > 95 and Arts > 35 and Literature > 35:
        if 2 in preference_list: #2=maths
            print("You are eligible for Accounts")
    else:
        print("you are not eligible for accounts ")

    

elif branch == "3":  # MECH
    if Maths > 90 and Literature > 90 and Arts > 35:
        if 2 in preference_list or 3 in preference_list: #2= maths,3=Literature
            print("You are eligible for Sales")
    else:
        print("You are not eligible for Sales")

    

else:
    print("Invalid branch entered. Please enter 1 for ECE, 2 for BCOM, or 3 for MECH.")