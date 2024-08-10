'''
Write a code to demonstrate use of inheritance and polymorphism using below example:
1. Eatable
1.1 Vegetarian
1.2 Non-Vegetarian
properties to be used: carbs, fat, protein, isPeelable, isBoneless
Place appropriate properties in parent class or child class and assign the values in _init_
'''

class eatable:
    def __init__(self,carbs,fat,protein):
        self.carbs=carbs
        self.fat=fat
        self.protein=protein

    def item(self):
        return "IT IS EATABLE"
        

class vegetarian(eatable):
    def __init__(self,carbs,fat,protein,is_peelable):
        super().__init__(carbs,fat,protein)
        self.is_peelable=is_peelable

    def item(self):
        return "IT IS VEGETARIAN"
        

class non_veg(eatable):
    def __init__(self,carbs,fat,protein,is_boneless):
        super().__init__(carbs,fat,protein)
        self.is_boneless=is_boneless

    def item(self):
        return "IT IS NON-VEGETARIAN"
        

def main():

    carbs=int(input("Enter the amount of carbs in grams"))
    fat=int(input("Enter the amount of fat in grams"))
    protein=int(input("Enter the amount of protein in grams"))
    is_peelable = input("Is it peelable? (yes/no): ").strip().lower()
    is_boneless = input("Is it boneless? (yes/no): ").strip().lower()
    if is_peelable == 'yes':
        item = vegetarian(carbs, fat, protein, is_peelable == 'yes')
    elif is_boneless == 'yes':
        item = non_veg(carbs, fat, protein, is_boneless == 'yes')
    else:
        print("Invalid input or item type not recognized.")
        return
    
if __name__ == "__main__":
    main()