class person:
    def __init__(self,age,gender,pincode):
        self.age=age
        self.gender=gender
        self.pincode

class student(person):
    def __init__(self,gender,age,pincode,residence):
        super().__init__(self,age,pincode)
        self.residence=residence
    def __init__(self,gender,age,pincode,residence, isquota):
        super().__init__(self,age,pincode)
        self.residence=residence
        print("sports quota")

class employee(person):
    def __init__(self,age,gender,pincode):
          super().__init__(age, gender, pincode)
student=student("25","female","123456","H")
student=student("25","female","123456","H","True")
        

