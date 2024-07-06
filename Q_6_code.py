'''
Write python program that swap two number with temp variable and 
without temp variable.
'''

n1 = int(input("Please Enter Number 1 : "))
n2 = int(input("Please Enter Number 2 : "))

print("Swap without Using Temp Variable")

n1= n1*n2
n2= n1/n2
n1= n1/n2

print("Now Number 1 Is ",int(n1))
print("And Number 2 Is ",int(n2))

print("Swap Using Temp Variable")

temp = n1
n1 = n2
n2 = temp

print("Now Number 1 Is ",int(n1))
print("And Number 2 Is ",int(n2))