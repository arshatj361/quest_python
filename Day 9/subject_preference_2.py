class Student:
    def __init__(self, arts, maths, literature, preferences):
        self.arts = arts
        self.maths = maths
        self.literature = literature
        self.preferences = preferences
  

class ECEStudent(Student):
    def check_eligibility(self):
        if self.arts > 90 and self.literature > 90 and self.maths > 35:
            if 1 in self.preferences or 3 in self.preferences:
                return "You are eligible for Marketing"
        elif self.arts>35 and self.maths>35 and self.literature>95:
            if 3 in self.preference:
                return "You are also eligible for HR"0
            +
        return "You are not eligible for Marketing"

class BCOMStudent(Student):
    def check_eligibility(self):
        if self.maths > 95 and self.arts > 35 and self.literature > 35:
            if 2 in self.preferences:
                return "You are eligible for Accounts"
        return "You are not eligible for Accounts"

class MECHStudent(Student):
    def check_eligibility(self):
        if self.maths > 90 and self.literature > 90 and self.arts > 35:
            if 2 in self.preferences or 3 in self.preferences:
                return "You are eligible for Sales"
        return "You are not eligible for Sales"

def main():
    
    branch = input("1. ECE\n2. BCOM\n3. MECH\nEnter your branch: ").strip()
    arts = int(input("Enter your marks in Arts: "))
    maths = int(input("Enter your marks in Maths: "))
    literature = int(input("Enter your marks in Literature: "))

   
    preference = input("1. Arts\n2. Maths\n3. Literature\n4.HR \nEnter your preferences with commas: ").strip()
    preference_list = [int(item) for item in preference.split(',')]

    
    if branch == "1":
        student = ECEStudent(arts, maths, literature, preference_list)
    elif branch == "2":
        student = BCOMStudent(arts, maths, literature, preference_list)
    elif branch == "3":
        student = MECHStudent(arts, maths, literature, preference_list)
    else:
        print("Invalid branch entered. Please enter 1 for ECE, 2 for BCOM, or 3 for MECH.")
        return

    
    print(student.check_eligibility())

if __name__ == "__main__":
    main()