'''
Write a Python function that takes a list of words and returns the length 
of the longest one
'''

def longest_word(words):
    max_length = 0
    
    for word in words:
        if len(word) > max_length:
            max_length = len(word)
    return max_length

word_list = []

for i in range(5):
    word = input("Please enter Word : ")
    word_list.append(word)
    
result = longest_word(word_list)
print(f"The length of the longest word is: {result}")
