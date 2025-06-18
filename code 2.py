#  Write a Python program to do arithmetical operations addition and division.
a = float(input("Enter the number :"))
b = float(input("Enter the number :"))
addition = a + b 
print(f"the value of addition:{addition}")
if b == 0 :
    print("Zero divison Error")
else:
    print(f"the value of division : {a/b}")
