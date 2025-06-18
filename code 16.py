# Write a Python Program to Find the Factorial of a Number.

Number = int(input("enter the Number : "))
factorial = 1
if Number <0:
    print("the factorial is not possible ")
elif Number == 0:
    print("The factorial is : 1")
elif Number == 1:
    print("The factorial is : 1 ")
else:
    for i in range(1,Number+1):
        factorial = factorial*i
    print(f"This is the factoral number {Number}: {factorial}") 

    
