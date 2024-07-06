#  Write a Python program to get the Fibonacci series of given range.

a,b = 0,1
num = int(input("Please Enter Any Number : "))

print(a," ",end="")

while b<num:
    a,b=b,a+b        
    print(b," ",end="")
    
