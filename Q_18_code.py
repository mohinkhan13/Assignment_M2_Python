'''
Write a Python program to add 'ing' at the end of a given string (length 
should be at least 3). If the given string already ends with 'ing' then add 
'ly' instead if the string length of the given string is less than 3, leave it 
unchanged.

'''

stri = input("Please Enter Any Word : ")
last = stri[-3:]

if len(stri) < 3:
    print("length should be at least 3")
elif last == "ing":
    stri += "ly"
    print(stri)
else:
    stri += "ing"
    print(stri)
