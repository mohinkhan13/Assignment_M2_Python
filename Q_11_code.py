'''
Write a python program to sum of the first n positive integers.

'''

n = int(input("Please Enter Number : "))
result = 0

for i in range (1,n+1):
    result+=i

for i in range (1,n+1):
    if i != n:
        print(i, " + ",end="")
    else:
        print(i, end=" ")
        

print("=",result)