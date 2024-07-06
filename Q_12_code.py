'''
Write a Python program to calculate the length of a string.

'''

string = input("Please Entre A String : ")

print(string)

count = 0
space = 0

for i in string:
    if i.isspace():
        count-=1
        space+=1
    else:
        count+=1
print("Without Space Your String Lenth is : ",count+1)
print("With Space Your String Lenth is : ",count+space+1)
