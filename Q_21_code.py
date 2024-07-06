# Write a Python function to reverses a string if its length is a multiple of 4

def reverse(s):
    if len(s) % 4 == 0:
        return s[::-1]
    else:
        return s

input_string = input("Please enter a string: ")
result = reverse(input_string)
print(f"The resulting string is: {result}")
