class OddEven:
    

    @staticmethod
    def oddEven():
        val = int(input("Enter a number: "))
        if val % 2 == 0:
            print(val, "is Even number")
        else:
            print(val, "is Odd number")
