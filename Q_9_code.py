'''
 Write a Python program to sum of three given integers. However, if
two values are equal sum will be zero.

'''

n1 = int(input("Enter N1 : "))
n2 = int(input("Enter N2 : "))
n3 = int(input("Enter N3 : "))

sum = 0
if n1 == n2 or n1 == n3 or n2==n3:
    print(sum)
else:
    sum = n1+n2+n3
    print(sum)