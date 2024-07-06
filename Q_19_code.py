'''
Write a Python program to find the first appearance of the substring 
'not' and 'poor' from a given string, if 'not' follows the 'poor', replace the 
whole 'not'...'poor' substring with 'good'. Return the resulting string.
'''

def replace_not_poor(s):
    Not = s.find("not")
    poor = s.find("poor")
    
    if Not != -1 and poor != -1 and poor > Not:
        s = s[:Not] + "good" + s[poor + 4:]
    return s

str = input("Please Enter A String : ")
result = replace_not_poor(str)
print(result) 
