'''
* Name

* Age
 
15% discount for all product for senior citizen
 
* Gender

male senior citizen (60 and above)

female senior citizen (45 and above)
 
100 rupees nyka, fastrack, if female (<45)

100 coupon on titan, fastrack, if male (<60)

----
 
*Occupation: Working, Student (PIN code should be local)
 
College: 500 coupon on books

Working: NA
 
----

*Residence: Hosteller, Localite (Hostel name should be valid)
 
Hosteller: Groceries

Localite: NA
 
----

* Armed Forces: Yes/No (Check from external file)
 
Yes: Free pass for R-day parade for 2

No: Na
 

 '''

#_____________________________________________________________________________________________________________________________________________

age=int(input("enter the age")) 
gender=input("\nM.male \nF.female \n Enter your gender: ")
occupancy=input("\nH.hosteller \n.L.localite \nEnter your occupancy: ")
status=input("\nW.working \nS.student  \nEnter your current status: ")
parents=input("\nY.yes\nN.no\n Parents working in armed forces yes/no:")
discount_pins=[301,302,303,304,305,306]
original_pincode=123456
if age>=60 and gender.lower()=="m": 
      print("senior citizen discount applied,thank you for shopping")
elif age>=45 and gender.lower()=="f":
        print("senior citizen discount applied,thank you for shopping")
elif age<45 and gender.lower()=="f" and occupancy.lower()=="h":
             print("Discount of Rs.100 Nyka")
             print("free groceries for hosteller")
             if status.lower()=="s":
                    discount_pin=int(input("enter your discount pin: "))
                    if discount_pin in discount_pins:
                            print("Rs.500 coupon for books")
                    else:
                            print("enter a valid discount pin for Rs.500 coupon for books")
             elif status.lower()=="w":
                    print("free groceries")  
elif age<45 and gender.lower()=="f" and occupancy.lower()=="l":
             print("Discount of Rs.100 Nyka")
             if status.lower()=="s":
                    discount_pin=int(input("enter your discount pin: "))
                    if discount_pin in discount_pins:
                            print("Rs.500 coupon for books")
                    else:
                            print("enter a valid discount pin for Rs.500 coupon for books")

elif age<60 and gender.lower()=="m" and occupancy.lower()=="h":
             print("Rs.100 coupon on Titan and Fastrack Watches!!")
             print("free groceries for hosteller")
             if status.lower()=="s":
                    discount_pin=int(input("enter your discount pin: "))
                    if discount_pin in discount_pins:
                            print("Rs.500 coupon for books")
                    else:
                            print("enter a valid discount pin for Rs.500 coupon for books")
                    
             elif status.lower()=="w":
                    print("Free groceries")
elif age<60 and gender.lower()=="m" and occupancy.lower()=="l":
             print("Rs.100 coupon on Titan and Fastrack Watches!!")
             if status.lower()=="s":
                    discount_pin=int(input("enter your discount pin: "))
                    if discount_pin in discount_pins:
                            print("Rs.500 coupon for books")
                    else:
                            print("enter a valid discount pin for Rs.500 coupon for books")

if parents.lower()=="y":
             print("Free pass fot R day parade for 2")