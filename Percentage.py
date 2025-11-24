class calculatePercentage:

    @staticmethod
    def FindPercentage():
        sub1 = int(input("Subject 1:"))
        sub2 = int(input("Subject 2:"))
        sub3 = int(input("Subject 3:"))
        sub4 = int(input("Subject 4:"))
        sub5 = int(input("Subject 5:"))

        total = sub1 + sub2 + sub3 + sub4 + sub5
        percentage = total / 5

        print("Subject1 =", sub1)
        print("Subject2 =", sub2)
        print("Subject3 =", sub3)
        print("Subject4 =", sub4)
        print("Subject5 =", sub5)
        print("Total =", total)
        print("Percentage =", percentage)
