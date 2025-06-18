#  Program 9
#  Write a Python program to solve quadratic equation.

import math

a = int(input("Enter the number :"))
b = int(input("Enter the number :"))
c = int(input("Enter the number :"))
"""D = b**2-4*a*c
if (d>0), the equation has two distinct real root 
if (d=0), the equation has one repeated real root 
if (d<0), the equation has complex roots.
 """

D = b**2-4*a*c
print(f" That Discriminant of the qeuation is :{D}")

if D>0:
    root_1 = (-b+math.sqrt(D))/(2*a)
    root_2 = (-b+math.sqrt(D))/(2*a)
    print(f"Root-1 :{root_1}")
    print(f"Root-2 :{root_2}")
elif D == 0:
    root = -b/(2*a)
    print(f"Root:{root}")
else:
    real_part = -b/(2*a)
    imaginary_part = math.sqrt(abs(D))/(2*a)
    print(f"Root-1:{real_part}+{imaginary_part}i")
    print(f"Root-2:{real_part}+{imaginary_part}j")