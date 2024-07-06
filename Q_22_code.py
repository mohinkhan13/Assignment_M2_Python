'''
Write a Python program to get a string made of the first 2 and the last 
2 chars from a given a string. If the string length is less than 2, return 
instead of the empty string.

'''

def first_last_2_chars(s):
    if len(s) < 2:
        return ""
    else:
        return s[:2] + s[-2:]

input_string = input("Please enter a string: ")
result = first_last_2_chars(input_string)
print(f"The resulting string is: {result}")
