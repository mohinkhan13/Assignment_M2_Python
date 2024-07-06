'''
Write a Python program to count occurrences of a substring in a string.

'''

main_string = input("Please enter the main string: ")
substring = input("Please enter the substring to count: ")

count = main_string.count(substring)

print('The substring ',substring,' appears', count, 'times in the main string.')
