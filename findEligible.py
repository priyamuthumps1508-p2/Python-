class EligibilityForMarriage:

    @staticmethod
    def Eligible():
        gender = input("Enter your Gender:")
        age = int(input("Enter your age:"))
        if gender == 'male' and age < 21:
            print("Your Gender:", gender)
            print("Your Age:", age)
            print("Not Eligible")

        elif gender == 'female' and age < 18:
            print("Your Gender:", gender)
            print("Your Age:", age)
            print("Not Eligible")
