'''
• Write a Python function to insert a string in the middle of a string.
'''
def insert_center(original, to_insert):

    middle_index = len(original) // 2
    result = original[:middle_index] + to_insert + original[middle_index:] 
    return result

# Example usage
str = input("Please enter the original string: ")
new_str = input("Please enter the string to insert: ")
result = insert_center(str, new_str)
print(f"The resulting string is: {result}")
