#  Write a Python program to get the Factorial number of given number.

num = int(input("Please Enter Any Number : "))
fact=1
for i in range(1,num+1):
    fact = fact*i
    print(fact)
