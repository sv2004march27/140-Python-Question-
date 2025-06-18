#  Write a Python Program to Check Leap Year.
Year = int(input("Enter the Year:"))
if (Year%400==0)and(Year/100==0):
    print(f"This is the leap year".format(Year))
elif (Year%4==0) and (Year/10!=0):
    print(f"This is the leap Year".format(Year))
else:
    print(f"This is not the leap year ".format(Year))
    

