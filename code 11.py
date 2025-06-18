#  Write a Python Program to Check if a Number is Positive, Negative or Zero.
number = float(input("Enter the number :"))
if number>0:
    print(f"This {number} is  Positive ")
elif number == 0:
    print(f"This {number}  is zero")
elif number<0:
    print(f"This {number} is negative")
else:
    print("you enter the wrong number !")
