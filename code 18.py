#  Program 18
#  Write a Python Program to Print the Fibonacci sequence.
#  Fibonacci sequence:
#  The Fibonacci sequence is a series of numbers where each number is the sum of the two
#  preceding ones, typically starting with 0 and 1. So, the sequence begins with 0 and 1, and
#  the next number is obtained by adding the previous two numbers. This pattern continues
#  indefinitely, generating a sequence that looks like this:
#  0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, and so on.
#  Mathematically, the Fibonacci sequence can be defined using the following recurrence
#  relation:
#  𝐹(0) = 0 𝐹(1) = 1 𝐹(𝑛) = 𝐹(𝑛−1)+𝐹(𝑛−2)𝑓𝑜𝑟𝑛 > 1

terms = int(input("Enter the terms :"))
n_0 = 0 
n_1 = 1
n_2 = 1 
count = 0 
if terms <= 0:
    print("pls enter the positive number ")
elif terms == 1:
    print(n_2)
else:
    print("fib Seq : ")

while count <= terms:
    print(n_0)
    sum = n_0 + n_1
    n_0 = n_1
    n_1 = sum
    count += 1 



    # print(n_2)
    # n_th = n_1 + n_2
    # n_1 = n_2
    # n_2 = n_th
    # count += 1

