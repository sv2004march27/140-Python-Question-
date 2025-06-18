#  Write a Python Program to Check Prime Number.
#  Prime Numbers:
#  A prime number is a whole number that cannot be evenly divided by any other number
#  except for 1 and itself. For example, 2, 3, 5, 7, 11, and 13 are prime numbers because they
#  cannot be divided by any other positive integer except for 1 and their own value.

number = int(input("enter the number :"))
i = 2
flag = 1
for i in range(2, number):
    if (number % i) == 0:
            flag = 0
            break 

if flag == 0:
    print("Not Prime")
else:
    print("Prime")
    
