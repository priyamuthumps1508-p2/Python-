class EligibilityForMarriage:

    @staticmethod
    def Eligible():      
        gender=input("Enter your Gender:")
        age=int(input("Enter your Age:"))
        if(gender=='Male' and age>=21):
            print("Your Gender is:",gender)
            print("Your age is:",age)
            print("Eligible")
        elif(gender=='Female' and age>=18):
            print("Your Gender is:",gender)
            print("Your age is:",age)
            print("Eligible")
        else:
            print("Your Gender is:",gender)
            print("Your age is:",age)
            print("Not Eligible")
        