'''
Write a Python program to get a single string from two given strings, 
separated by a space and swap the first two characters of each string
'''

str1 = input("please Enter Str1 : ")
str2 = input("please Enter Str2 : ")

    
new_s1 = str2[:2] + str1[2:]
new_s2 = str1[:2] + str2[2:]

result = new_s1 + " " + new_s2
print( result)

