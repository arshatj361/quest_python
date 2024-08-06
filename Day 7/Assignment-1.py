age=int(input("enter the age")) 
gender=input("\nM.male \nF.female \n Enter your gender: ")
occupancy=input("\nH.hosteller \n.L.localite \nEnter your occupancy: ")
status=input("\nW.working \nS.student  \nEnter your current status: ")
parents=input("\nY.yes\nN.no\n Parents working in armed forces yes/no:")
if age>=60 and gender.lower()=="m": 
      print("senior citizen discount applied,thank you for shopping")
elif age>=45 and gender.lower()=="f":
        print("senior citizen discount applied,thank you for shopping")
elif age<45 and gender.lower()=="f" and occupancy.lower()=="h":
             print("Discount of Rs.100 Nyka")
             if status.lower()=="s":
                    print("Rs.500 coupon for books")
             else:
                    print("free groceries")  
elif age<45 and gender.lower()=="f" and occupancy.lower()=="l":
             print("Discount of Rs.100 Nyka")
             if status.lower()=="s":
                    print("Rs.500 coupon for books")
             else:
                    print("No discount available")

elif age<60 and gender.lower()=="m" and occupancy.lower()=="h":
    print("Rs.100 coupon on Titan and Fastrack Watches!!")
    if status.lower()=="s":
             print("Rs.500 coupon for books")
    else:
            print("Free groceries")
elif age<60 and gender.lower()=="m" and occupancy.lower()=="l":
    print("Rs.100 coupon on Titan and Fastrack Watches!!")
    if status.lower()=="s":
             print("Rs.500 coupon for books")
    else:
            print("No discount available")
if parents.lower()=="y":
      print("Free pass fot R day parade for 2")


 
                  
